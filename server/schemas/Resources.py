from pydantic import BaseModel
from datetime import datetime
from config.enums.audience import AudienceEnum


class ResourcesBase(BaseModel):
    audience: AudienceEnum
    title: str
    description: str
    author_id: int


class ResourceCreate(ResourcesBase):
    pass


class Resources(ResourcesBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True