from pydantic import BaseModel
from datetime import datetime


class ConsumableMacrosBase(BaseModel):
    consumable_id: int
    macro_type_id: int
    quantity: float


class ConsumableMacrosCreate(ConsumableMacrosBase):
    pass


class ConsumableMacros(ConsumableMacrosBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True