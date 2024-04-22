from pydantic import BaseModel
from datetime import datetime
from config.enums.booked import BookedEnum
from schemas.Consumables import Consumable
from schemas.Users import User


class SurplusListingBase(BaseModel):
    consumable_id: int
    price: float
    booked: BookedEnum = BookedEnum.NOT_BOOKED


class SurplusListingCreate(SurplusListingBase):
    farmer_id: int


class SurplusListing(SurplusListingBase):
    id: int
    farmer: User
    consumable: Consumable
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
