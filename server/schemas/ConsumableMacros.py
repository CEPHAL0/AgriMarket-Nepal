from pydantic import BaseModel
from datetime import datetime


class ConsumableMacroBase(BaseModel):
    consumable_id: int
    macro_type_id: int
    quantity: float


class ConsumableMacroCreate(ConsumableMacroBase):
    pass


class ConsumableMacro(ConsumableMacroBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
