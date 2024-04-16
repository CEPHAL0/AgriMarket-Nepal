from pydantic import BaseModel
from datetime import datetime

class ProvinceBase(BaseModel):
    name: str


class ProvinceCreate(ProvinceBase):
    pass


class Province(ProvinceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
