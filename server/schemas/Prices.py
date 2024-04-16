from pydantic import BaseModel
from datetime import datetime

class PricesBase(BaseModel):
    consumable_id: int
    price: float


class PriceCreate(PricesBase):
    pass


class Prices(PricesBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True