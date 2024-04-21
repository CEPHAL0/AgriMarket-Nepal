from pydantic import BaseModel
from datetime import datetime


class ConsumableListingBase(BaseModel):
    consumable_id: int
    user_id: int
    price: float
    district_id: int
    quantity: float


class ConsumableListingCreate(ConsumableListingBase):
    expiry_date: datetime


class ConsumableListing(ConsumableListingBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
