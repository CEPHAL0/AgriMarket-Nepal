from pydantic import BaseModel
from enum import Enum

class ConsumableTypeEnum(str, Enum):
    vegetable = "VEGETABLE"
    fruit = "FRUIT"
    dairy = "DAIRY"
    other = "OTHER"


class ConsumablesBase(BaseModel):
    name: str
    type: ConsumableTypeEnum


class ConsumablesCreate(ConsumablesBase):
    pass


class Consumables(ConsumablesBase):
    id: int

    class Config:
        orm_mode = True