from pydantic import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """
    应用程序配置
    """
    # API配置
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "TAPD MCP Server"
    
    # TAPD API配置
    TAPD_API_USER: str = os.getenv("TAPD_API_USER", "")
    TAPD_API_PASSWORD: str = os.getenv("TAPD_API_PASSWORD", "")
    
    # 分页配置
    DEFAULT_PAGE_SIZE: int = 30
    MAX_PAGE_SIZE: int = 100

    class Config:
        case_sensitive = True

settings = Settings() 