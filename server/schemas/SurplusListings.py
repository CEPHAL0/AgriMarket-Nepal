from pydantic import BaseModel
from datetime import datetime
from config.enums.booked import BookedEnum

class SurplusListingsBase(BaseModel):
    consumable_id: int
    price: float
    booked: BookedEnum


class SurplusListingCreate(SurplusListingsBase):
    pass


class SurplusListings(SurplusListingsBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True