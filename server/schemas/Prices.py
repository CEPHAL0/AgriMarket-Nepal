from pydantic import BaseModel
from datetime import datetime


class PriceBase(BaseModel):
    consumable_id: int
    price: float


class PriceCreate(PriceBase):
    pass


class Price(PriceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
