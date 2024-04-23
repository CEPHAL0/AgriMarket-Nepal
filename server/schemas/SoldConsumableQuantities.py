from pydantic import BaseModel
from datetime import datetime
from schemas.Consumables import Consumable
from schemas.Users import User


class SoldConsumableQuantityBase(BaseModel):
    consumable_id: int
    farmer_id: int
    quantity_sold: float
    date_sold: datetime


class SoldConsumableQuantityCreate(SoldConsumableQuantityBase):
    pass


class SoldConsumableQuantity(SoldConsumableQuantityBase):
    id: int
    consumable: Consumable
    farmer: User
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
