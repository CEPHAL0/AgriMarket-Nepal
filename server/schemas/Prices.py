from pydantic import BaseModel
from datetime import datetime
from schemas.Consumables import Consumable


class PriceBase(BaseModel):
    consumable_id: int
    price: float
    date: datetime


class PriceCreate(PriceBase):
    pass


class Price(PriceBase):
    id: int
    consumable: Consumable
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
