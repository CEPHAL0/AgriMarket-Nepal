from pydantic import BaseModel
from datetime import datetime

class ProvincesBase(BaseModel):
    name: str


class ProvincesCreate(ProvincesBase):
    pass


class Provinces(ProvincesBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True