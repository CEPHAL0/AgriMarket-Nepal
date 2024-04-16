from pydantic import BaseModel
from datetime import datetime


class ResourceImagesBase(BaseModel):
    resource_id: int
    image_path: str
    order: int


class ResourceImageCreate(ResourceImagesBase):
    pass


class ResourceImages(ResourceImagesBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True