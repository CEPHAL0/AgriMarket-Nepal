from pydantic import BaseModel
from datetime import datetime
from config.enums.audience import AudienceEnum


class ResourceBase(BaseModel):
    audience: AudienceEnum
    title: str
    description: str
    author_id: int


class ResourceCreate(ResourceBase):
    pass


class Resource(ResourceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
