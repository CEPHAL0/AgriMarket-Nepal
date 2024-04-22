from pydantic import BaseModel
from datetime import datetime
from schemas.Districts import District
from schemas.Users import User
from schemas.Consumables import Consumable
from schemas.Users import User


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
    consumable: Consumable
    district: District
    user: User
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
