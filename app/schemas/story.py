from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class StoryBase(BaseModel):
    """
    需求基础模型
    """
    name: str = Field(..., description="需求标题")
    description: Optional[str] = Field(None, description="需求描述")
    workspace_id: int = Field(..., description="项目ID")
    status: Optional[str] = Field(None, description="需求状态")
    priority: Optional[str] = Field(None, description="优先级")
    iteration_id: Optional[str] = Field(None, description="迭代ID")
    owner: Optional[str] = Field(None, description="负责人")

class StoryCreate(StoryBase):
    """
    创建需求的请求模型
    """
    pass

class StoryUpdate(BaseModel):
    """
    更新需求的请求模型
    """
    name: Optional[str] = Field(None, description="需求标题")
    description: Optional[str] = Field(None, description="需求描述")
    status: Optional[str] = Field(None, description="需求状态")
    priority: Optional[str] = Field(None, description="优先级")
    iteration_id: Optional[str] = Field(None, description="迭代ID")
    owner: Optional[str] = Field(None, description="负责人")

class Story(StoryBase):
    """
    需求完整模型
    """
    id: str = Field(..., description="需求ID")
    created: datetime = Field(..., description="创建时间")
    modified: datetime = Field(..., description="修改时间")
    creator: str = Field(..., description="创建人")
    
    class Config:
        orm_mode = True 