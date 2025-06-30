import discord
import asyncio
import threading
import aiohttp
import os
from pathlib import Path
from datetime import datetime
from typing import List, Optional, Dict, Any, Union
import sys

import sys
from pathlib import Path
sys.path.append(str(Path.cwd()))
from config.config import settings

from mcp.server.fastmcp import FastMCP
from typing import Union

from logging import getLogger
logger=getLogger(__name__)

class DiscordService:
    _instance = None
    
    def __init__(self, token: str):
        if DiscordService._instance is not None:
            raise RuntimeError("DiscordService is a singleton! Use DiscordService.get_instance()")
        
        self.token = token
        self.loop = asyncio.new_event_loop()
        self.ready_event = threading.Event()
        self.client = None
        self.thread = threading.Thread(target=self._run_bot, daemon=True)
        self.thread.start()
        self.download_path = Path(settings.DISCORD_DOWNLOAD_PATH)
        self.download_path.mkdir(parents=True, exist_ok=True)
        DiscordService._instance = self

    @classmethod
    def get_instance(cls, token: str = None):
        if cls._instance is None:
            if token is None:
                raise ValueError("Token must be provided for first initialization")
            cls._instance = cls(token)
        return cls._instance

    def _run_bot(self):
        asyncio.set_event_loop(self.loop)

        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        intents.guild_messages = True

        self.client = discord.Client(intents=intents, loop=self.loop)

        @self.client.event
        async def on_ready():
            print(f"Logged in as {self.client.user} (ID: {self.client.user.id})")
            self.ready_event.set()

        async def start():
            await self.client.start(self.token)

        try:
            self.loop.run_until_complete(start())
        except Exception as e:
            print(f"Bot encountered an error: {e}")
        finally:
            asyncio.set_event_loop(None)

    def _run_coro(self, coro):
        self.ready_event.wait()
        if not self.loop.is_running():
            raise RuntimeError("Event loop is not running")
        future = asyncio.run_coroutine_threadsafe(coro, self.loop)
        return future.result()

    def list_servers(self) -> List[Dict[str, Any]]:
        async def coro():
            servers = []
            for guild in self.client.guilds:
                servers.append({
                    'id': guild.id,
                    'name': guild.name,
                    'member_count': guild.member_count,
                    'owner_id': guild.owner_id
                })
            return servers
        return self._run_coro(coro())

    def list_channels(self, server_id: int) -> List[Dict[str, Any]]:
        async def coro():
            guild = self.client.get_guild(server_id)
            if not guild:
                return []
            
            channels = []
            for channel in guild.channels:
                if not isinstance(channel, discord.TextChannel):
                    continue
                channel_info = {
                    'id': channel.id,
                    'name': channel.name,
                    'type': str(channel.type),
                    'category': channel.category.name if channel.category else None,
                    'position': channel.position,
                    'topic': channel.topic,
                    'nsfw': channel.nsfw,
                }
                channels.append(channel_info)
            return channels
        return self._run_coro(coro())

    def _format_messages(self, messages: list) -> list:
        """
        Format messages from single channel into a single string.
        
        Args:
            messages: list with keys: ['id', 'content', 'timestamp', 'author', 'attachments']
            
        Returns:    
            list(str): Formatted list of messages string with author

            e.g. ["<user-name>: <user-message>", ...]
        """
        formatted_messages = []
        for msg in messages:
            author = msg['author']['display_name'] or msg['author']['name']
            content = msg['content']
            formatted_messages.append(f"{author}: {content}")

        formatted_messages.append("")  # Empty line between channels

        return formatted_messages


    def read_messages(
        self,
        channel_id: int,
        limit: int = 100,
        after: Optional[datetime] = None,
        before: Optional[datetime] = None,
        download_attachments: bool = False,
        format_messages: bool = True,
    ) -> List[Dict[str, Any]]:
        async def coro():
            channel = self.client.get_channel(channel_id)
            if not channel or not isinstance(channel, discord.TextChannel):
                return []
            
            messages = []
            try:
                async for message in channel.history(
                    limit=limit,
                    after=after,
                    before=before
                ):
                    msg_data = {
                        'id': message.id,
                        'content': message.content,
                        'timestamp': message.created_at,
                        'author': {
                            'id': message.author.id,
                            'name': message.author.name,
                            'display_name': message.author.display_name
                        },
                        'attachments': []
                    }
                    
                    for attachment in message.attachments:
                        att_data = {
                            'id': attachment.id,
                            'filename': attachment.filename,
                            'url': attachment.url,
                            'size': attachment.size
                        }
                        if download_attachments:
                            try:
                                path = await self._download_attachment(attachment, channel_id, message.id)
                                att_data['local_path'] = str(path)
                            except Exception as e:
                                att_data['error'] = str(e)
                        msg_data['attachments'].append(att_data)
                    
                    messages.append(msg_data)
            except Exception as ex:
                logger.error(f"error getting messages for channel: {channel_id} : {ex}")
            if format_messages:
                return self._format_messages(messages)
            return messages
        return self._run_coro(coro())

    async def _download_attachment(
        self,
        attachment: discord.Attachment,
        channel_id: int,
        message_id: int
    ) -> Path:
        """Download an attachment to local storage"""
        channel_dir = self.download_path / str(channel_id)
        message_dir = channel_dir / str(message_id)
        message_dir.mkdir(parents=True, exist_ok=True)
        
        filename = self._sanitize_filename(attachment.filename)
        file_path = message_dir / filename
        
        async with aiohttp.ClientSession() as session:
            async with session.get(attachment.url) as resp:
                if resp.status == 200:
                    with open(file_path, 'wb') as f:
                        async for chunk in resp.content.iter_chunked(8192):
                            f.write(chunk)
                    return file_path
                raise Exception(f"Download failed: HTTP {resp.status}")

    def _sanitize_filename(self, filename: str) -> str:
        """Make filename safe for filesystem"""
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        if len(filename) > 200:
            name, ext = os.path.splitext(filename)
            filename = name[:200 - len(ext)] + ext
        return filename

    def post_message(
        self,
        channel_id: int,
        content: str,
        files: Optional[List[Union[str, Path]]] = None
    ) -> bool:
        async def coro():
            channel = self.client.get_channel(channel_id)
            if not channel or not isinstance(channel, discord.TextChannel):
                return False
                
            try:
                if files:
                    discord_files = []
                    for file_path in files:
                        path = Path(file_path)
                        if path.is_file():
                            discord_files.append(discord.File(path))
                    await channel.send(content=content, files=discord_files)
                else:
                    await channel.send(content)
                return True
            except Exception as e:
                print(f"Error sending message: {e}")
                return False
        return self._run_coro(coro())

    def shutdown(self):
        async def close():
            await self.client.close()
        if self.loop.is_running():
            self._run_coro(close())
            self.loop.call_soon_threadsafe(self.loop.stop)

# Initialize global instance
try:
    discord_service = DiscordService.get_instance(settings.DISCORD_TOKEN)
except RuntimeError:
    # Already initialized
    discord_service = DiscordService._instance


mcp = FastMCP("DiscordBot")

@mcp.tool()
def list_channels() -> list[int]:
    """List accessible Discord channels (returns IDs as strings)"""
    # return runner.run_operation(list_channels_operation)
    return settings.DISCORD_CHANNELS

@mcp.tool()
def read_messages(channel_id: Union[int, str], limit: int = 10) -> list:
    """
    Read recent messages from a channel
    
    Args:
        channel_id: Discord channel ID (as string)
        limit: Number of messages to retrieve (max 100)
    """
    channel_id = int(channel_id)
    print(f"\n\n channel_id: {channel_id}")
    messages = discord_service.read_messages(
            channel_id=channel_id, # channels[0]['id']
            limit=limit,
            download_attachments=False
        )
    print(f"\n\n read messages:{messages}")
    return messages

@mcp.tool()
def post_message(channel_id: int, message: str) -> bool:
    """
    Post message to a channel
    
    Args:
        channel_id: Discord channel ID (as string)
        message: Content to send
    """
    return discord_service.post_message(
        channel_id=channel_id, #channels[0]['id'],
        content=message
    )

# if __name__=="__main__":
#     # from bot import discord_service

#     # List all servers
#     servers = discord_service.list_servers()
#     print("Servers:", servers)

#     # List channels in first server
#     if servers:
#         channels = discord_service.list_channels(servers[0]['id'])
#         print(f"\n\nChannels in {servers[0]['name']}:", channels)

#     # Read messages from first channel
#     if channels:

#         messages = discord_service.read_messages(
#             channel_id=settings.DISCORD_CHANNELS[0], # channels[0]['id']
#             limit=5,
#             download_attachments=True
#         )
#         print(f"Messages in {settings.DISCORD_CHANNELS[0]}:", messages) # channels[0]['name']

#     # Send message to channel
#     if channels:
#         posted = discord_service.post_message(
#             channel_id=settings.DISCORD_CHANNELS[0], #channels[0]['id'],
#             content="Hello from the bot!"
#         )

if __name__ == "__main__":
    mcp.run()

