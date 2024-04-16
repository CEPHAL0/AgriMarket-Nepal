from pydantic import BaseModel
from datetime import datetime


class ConsumableListingsBase(BaseModel):
    consumable_id: int
    user_id: int
    price: float
    district_id: int


class ConsumableListingCreate(ConsumableListingsBase):
    pass


class ConsumableListings(ConsumableListingsBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True