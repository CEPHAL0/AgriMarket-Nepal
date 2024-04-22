from pydantic import BaseModel
from datetime import datetime


class ResourceImageBase(BaseModel):
    resource_id: int
    # image_path: str
    order: int


class ResourceImageCreate(ResourceImageBase):
    pass


class ResourceImage(ResourceImageBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
