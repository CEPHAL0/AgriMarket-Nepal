from pydantic import BaseModel
from datetime import datetime

class UserSurplusBookingBase(BaseModel):
    consumable_id: int
    poster_id: int
    booker_id: int


class UserSurplusBookingCreate(UserSurplusBookingBase):
    pass


class UserSurplusBooking(UserSurplusBookingBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True