from pydantic import BaseModel
from datetime import datetime

class DistrictBase(BaseModel):
    name: str
    province_id: int
    ecological_region: str


class DistrictCreate(DistrictBase):
    pass


class District(DistrictBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
