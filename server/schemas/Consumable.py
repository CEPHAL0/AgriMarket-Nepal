from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from config.enums.consumable import ConsumableEnum


class ConsumableTypeEnum(str, Enum):
    vegetable = "VEGETABLE"
    fruit = "FRUIT"
    dairy = "DAIRY"
    other = "OTHER"


class ConsumablesBase(BaseModel):
    name: str
    type: ConsumableEnum
    image_path: str


class ConsumablesCreate(ConsumablesBase):
    pass


class Consumable(ConsumablesBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
