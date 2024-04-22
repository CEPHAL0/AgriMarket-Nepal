from pydantic import BaseModel
from datetime import datetime
from config.enums.accepted import AcceptedEnum
from schemas.SurplusListings import SurplusListing


class UserSurplusBookingBase(BaseModel):
    surplus_listing_id: int
    booker_id: int


class UserSurplusBookingCreate(UserSurplusBookingBase):
    pass


class UserSurplusBooking(UserSurplusBookingBase):
    id: int
    surplus_listing: SurplusListing
    accepted: AcceptedEnum
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
