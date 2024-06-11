from pydantic import BaseModel
from datetime import datetime
from schemas.MacroTypes import MacroType
from schemas.Consumables import Consumable


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
    macro_type: MacroType
    consumable: Consumable

    class Config:
        orm_mode = True
