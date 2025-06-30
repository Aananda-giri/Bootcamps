from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List
from pathlib import Path

import os
from dotenv import load_dotenv
load_dotenv()

class AppConfig(BaseSettings):
    # Telegram API
    INCLUDE_CONTEXT7_MCP: bool = Field(..., env='INCLUDE_CONTEXT7_MCP')
    MEMORY_PATH: str = Field("storage/memory.db", env='MEMORY_PATH')
    
    DISCORD_TOKEN:str = Field(..., env='DISCORD_TOKEN')
    # Search Terms
    DISCORD_CHANNELS: List[int] = Field(..., env='DISCORD_CHANNELS')
    LLM_TO_USE:str = Field(..., env='LLM_TO_USE')
    GEMINI_API_KEY:str = Field(..., env='GEMINI_API_KEY')
    INCLUDE_CONTEXT7_MCP:bool = Field(..., env='INCLUDE_CONTEXT7_MCP')

    # discord download path
    _download_path = Path(os.environ.get("DISCORD_DOWNLOAD_PATH", "Downloads/Discord"))
    _download_path.mkdir(parents=True, exist_ok=True)
    DISCORD_DOWNLOAD_PATH: Path = Field(_download_path, env='DISCORD_CHANNELS')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

# Create a global instance
settings = AppConfig()

# Usage in your code:
# from config import config
# api_id = config.telegram_api_id
# openai_key = config.openai_api_key
# firecrawl_key = config.firecrawl_api_key