from pydantic import BaseModel
from datetime import datetime
from config.enums.booked import BookedEnum

class SurplusListingBase(BaseModel):
    consumable_id: int
    price: float
    booked: BookedEnum


class SurplusListingCreate(SurplusListingBase):
    pass


class SurplusListing(SurplusListingBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
