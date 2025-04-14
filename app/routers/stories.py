from fastapi import APIRouter, HTTPException, Query, Path
from typing import Optional, Dict, Any, List
from ..core.config import settings
from ..schemas.story import Story, StoryCreate, StoryUpdate
from ..services.tapd_service import TapdService
import logging

logger = logging.getLogger(__name__)
router = APIRouter()
tapd_service = TapdService()

@router.get("/{workspace_id}", response_model=List[Story])
async def get_stories(
    workspace_id: int = Path(..., description="项目ID"),
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(settings.DEFAULT_PAGE_SIZE, le=settings.MAX_PAGE_SIZE, description="每页数量"),
    story_id: Optional[str] = Query(None, description="需求ID"),
    name: Optional[str] = Query(None, description="需求标题"),
    status: Optional[str] = Query(None, description="需求状态")
):
    """
    获取需求列表
    """
    try:
        options = {}
        if story_id:
            options["id"] = story_id
        if name:
            options["name"] = name
        if status:
            options["status"] = status
            
        stories = await tapd_service.get_stories(
            workspace_id=workspace_id,
            options=options
        )
        return stories
    except Exception as e:
        logger.error(f"获取需求列表失败: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{workspace_id}/{story_id}", response_model=Story)
async def get_story(
    workspace_id: int = Path(..., description="项目ID"),
    story_id: str = Path(..., description="需求ID")
):
    """
    获取需求详情
    """
    try:
        story = await tapd_service.get_story(
            workspace_id=workspace_id,
            story_id=story_id
        )
        if not story:
            raise HTTPException(status_code=404, detail="需求不存在")
        return story
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"获取需求详情失败: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 