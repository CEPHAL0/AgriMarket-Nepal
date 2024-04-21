from pydantic import BaseModel
from datetime import datetime


class SoldConsumableQuantityBase(BaseModel):
    consumable_id: int
    farmer_id: int
    quantity_sold: float
    date_sold: int


class SoldConsumableQuantityCreate(SoldConsumableQuantityBase):
    pass


class SoldConsumableQuantity(SoldConsumableQuantityBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
