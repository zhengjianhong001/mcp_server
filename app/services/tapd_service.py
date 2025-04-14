from typing import Optional, Dict, Any, List
import logging
from ..core.config import settings
from ..schemas.story import Story, StoryCreate, StoryUpdate
import json

logger = logging.getLogger(__name__)

class TapdService:
    """
    TAPD服务类，处理与TAPD API的交互
    """
    
    async def get_stories(
        self,
        workspace_id: int,
        options: Optional[Dict[str, Any]] = None
    ) -> List[Story]:
        """
        获取需求列表
        """
        try:
            # 调用MCP SDK获取需求列表
            from mcp.mcp_server.tapd import get_stories
            
            response = get_stories(
                workspace_id=workspace_id,
                options=options
            )
            
            # 解析响应数据
            response_data = json.loads(response)
            if response_data.get("status") != 1:
                raise Exception(response_data.get("info", "获取需求列表失败"))
                
            stories_data = response_data.get("data", [])
            stories = []
            for story_data in stories_data:
                story = story_data.get("Story", {})
                stories.append(Story(**story))
                
            return stories
            
        except Exception as e:
            logger.error(f"获取需求列表失败: {str(e)}")
            raise
            
    async def get_story(
        self,
        workspace_id: int,
        story_id: str
    ) -> Optional[Story]:
        """
        获取需求详情
        """
        try:
            # 调用MCP SDK获取需求详情
            from mcp.mcp_server.tapd import get_stories
            
            response = get_stories(
                workspace_id=workspace_id,
                options={"id": story_id}
            )
            
            # 解析响应数据
            response_data = json.loads(response)
            if response_data.get("status") != 1:
                raise Exception(response_data.get("info", "获取需求详情失败"))
                
            stories_data = response_data.get("data", [])
            if not stories_data:
                return None
                
            story_data = stories_data[0].get("Story", {})
            return Story(**story_data)
            
        except Exception as e:
            logger.error(f"获取需求详情失败: {str(e)}")
            raise 