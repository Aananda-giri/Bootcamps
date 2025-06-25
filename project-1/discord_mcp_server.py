import os
import json
import asyncio
import discord
import logging
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from threading import Thread

# Load environment variables
load_dotenv()
logger = logging.getLogger(__name__)

# Configure Discord intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

class DiscordBotRunner:
    """Runs Discord operations with channel restrictions"""
    def __init__(self):
        self.token = os.getenv('DISCORD_TOKEN')
        self.target_channels = self._get_target_channels()
    
    def _get_target_channels(self):
        """Parse allowed channels from environment"""
        try:
            channels = json.loads(os.getenv('DISCORD_CHANNELS', '[]'))
            if not isinstance(channels, list):
                raise ValueError("DISCORD_CHANNELS must be a list")
            return [int(c) for c in channels if str(c).isdigit()]
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            logger.error(f"Error parsing channels: {e}")
            return []

    async def _run_bot_operation(self, operation, *args, **kwargs):
        """Execute a bot operation with channel restrictions"""
        if not self.token:
            raise ValueError("DISCORD_TOKEN not set")
        
        bot = discord.Client(intents=intents)
        # Store target channels on the bot instance
        bot.target_channels = self.target_channels
        result = None

        @bot.event
        async def on_ready():
            nonlocal result
            try:
                result = await operation(bot, *args, **kwargs)
            except Exception as e:
                logger.error(f"Operation failed: {e}")
                result = {"error": str(e)}
            finally:
                await bot.close()

        try:
            await bot.start(self.token)
        except discord.LoginError:
            logger.error("Invalid DISCORD_TOKEN")
            result = {"error": "Authentication failed"}
        return result

    def run_operation(self, operation, *args, **kwargs):
        """Thread-safe wrapper for bot operations"""
        result_container = []
        
        def thread_target():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                result = loop.run_until_complete(
                    self._run_bot_operation(operation, *args, **kwargs)
                )
                result_container.append(result)
            except Exception as e:
                result_container.append({"error": str(e)})
            finally:
                loop.close()

        thread = Thread(target=thread_target)
        thread.start()
        thread.join()
        
        return result_container[0] if result_container else {"error": "No result"}


class DiscordBotRunner:
    """Runs Discord operations with channel restrictions"""
    def __init__(self):
        self.token = os.getenv('DISCORD_TOKEN')
        self.target_channels = self._get_target_channels()
    
    def _get_target_channels(self):
        """Parse allowed channels from environment"""
        try:
            channels = json.loads(os.getenv('DISCORD_CHANNELS', '[]'))
            if not isinstance(channels, list):
                raise ValueError("DISCORD_CHANNELS must be a list")
            
            # Convert all values to integers
            return [int(c) for c in channels]
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            logger.error(f"Error parsing channels: {e}")
            return []

    async def _run_bot_operation(self, operation, *args, **kwargs):
        """Execute a bot operation with channel restrictions"""
        if not self.token:
            raise ValueError("DISCORD_TOKEN not set")
        
        bot = discord.Client(intents=intents)
        result = None

        @bot.event
        async def on_ready():
            nonlocal result
            try:
                result = await operation(bot, *args, **kwargs)
            except Exception as e:
                logger.error(f"Operation failed: {e}")
                result = {"error": str(e)}
            finally:
                await bot.close()

        try:
            await bot.start(self.token)
        except discord.LoginError:
            logger.error("Invalid DISCORD_TOKEN")
            result = {"error": "Authentication failed"}
        return result

    def run_operation(self, operation, *args, **kwargs):
        """Thread-safe wrapper for bot operations"""
        result_container = []
        
        def thread_target():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                result = loop.run_until_complete(
                    self._run_bot_operation(operation, *args, **kwargs)
                )
                result_container.append(result)
            except Exception as e:
                result_container.append({"error": str(e)})
            finally:
                loop.close()

        thread = Thread(target=thread_target)
        thread.start()
        thread.join()
        
        return result_container[0] if result_container else {"error": "No result"}

# Discord operations
async def list_channels_operation(bot):
    """List accessible channels"""
    channels = []
    for channel_id in bot.target_channels:
        channel = bot.get_channel(channel_id)
        if not channel:
            try:
                channel = await bot.fetch_channel(channel_id)
            except discord.NotFound:
                continue
        
        # Return channel IDs as strings to avoid scientific notation
        channels.append({
            "id": str(channel.id),  # Convert to string
            "name": channel.name,
            "type": str(channel.type),
            "guild": channel.guild.name if hasattr(channel, 'guild') else None
        })
    return channels

async def read_messages_operation(bot, channel_id: int, limit: int = 10):
    """Read messages from a channel"""
    # Convert to int if needed
    if not isinstance(channel_id, int):
        try:
            channel_id = int(channel_id)
        except (TypeError, ValueError):
            return {"error": "Invalid channel ID format"}
    
    if channel_id not in bot.target_channels:
        return {"error": "Unauthorized channel access"}
    
    channel = bot.get_channel(channel_id) or await bot.fetch_channel(channel_id)
    messages = []
    async for msg in channel.history(limit=min(limit, 100)):
        messages.append({
            "id": str(msg.id),  # Convert to string
            "author": msg.author.name,
            "content": msg.content,
            "timestamp": msg.created_at.isoformat()
        })
    return messages[::-1]  # Oldest first

async def post_message_operation(bot, channel_id: int, message: str):
    """Post message to a channel"""
    # Convert to int if needed
    if not isinstance(channel_id, int):
        try:
            channel_id = int(channel_id)
        except (TypeError, ValueError):
            return {"error": "Invalid channel ID format"}
    
    if channel_id not in bot.target_channels:
        return {"error": "Unauthorized channel access"}
    
    channel = bot.get_channel(channel_id) or await bot.fetch_channel(channel_id)
    sent = await channel.send(message)
    return {"success": True, "message_id": str(sent.id)}  # Convert to string

# Create MCP server
mcp = FastMCP("DiscordBot")

# Tool definitions - update to use string IDs
@mcp.tool()
def list_channels() -> list:
    """List accessible Discord channels (returns IDs as strings)"""
    runner = DiscordBotRunner()
    return runner.run_operation(list_channels_operation)

@mcp.tool()
def read_messages(channel_id: str, limit: int = 10) -> list:
    """
    Read recent messages from a channel
    
    Args:
        channel_id: Discord channel ID (as string)
        limit: Number of messages to retrieve (max 100)
    """
    runner = DiscordBotRunner()
    return runner.run_operation(read_messages_operation, int(channel_id), min(limit, 100))

@mcp.tool()
def post_message(channel_id: str, message: str) -> dict:
    """
    Post message to a channel
    
    Args:
        channel_id: Discord channel ID (as string)
        message: Content to send
    """
    runner = DiscordBotRunner()
    return runner.run_operation(post_message_operation, int(channel_id), message)

if __name__ == "__main__":
    mcp.run()