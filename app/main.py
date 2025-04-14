from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Dict, Any
import logging
from .routers import stories
from .core.config import settings

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="TAPD MCP Server",
    description="TAPD平台的需求管理功能集成服务",
    version="1.0.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 包含路由
app.include_router(stories.router, prefix="/api/v1/stories", tags=["stories"])

@app.get("/")
async def root():
    """
    健康检查接口
    """
    return {"status": "ok", "message": "TAPD MCP Server is running"} 