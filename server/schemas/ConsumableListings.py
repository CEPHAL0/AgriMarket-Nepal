from pydantic import BaseModel
from datetime import datetime


class ConsumableListingBase(BaseModel):
    consumable_id: int
    user_id: int
    price: float
    district_id: int


class ConsumableListingCreate(ConsumableListingBase):
    pass


class ConsumableListing(ConsumableListingBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
