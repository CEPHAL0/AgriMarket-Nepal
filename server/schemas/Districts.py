from pydantic import BaseModel
from datetime import datetime

class DistrictsBase(BaseModel):
    name: str
    province_id: int
    ecological_region: str


class DistrictCreate(DistrictsBase):
    pass


class Districts(DistrictsBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True