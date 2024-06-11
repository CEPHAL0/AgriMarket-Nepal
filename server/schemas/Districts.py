from pydantic import BaseModel
from datetime import datetime
from schemas.Provinces import Province


class DistrictBase(BaseModel):
    name: str
    province_id: int
    ecological_region: str


class DistrictCreate(DistrictBase):
    pass


class District(DistrictBase):
    id: int
    province: Province
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
