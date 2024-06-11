from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from config.enums.consumable import ConsumableEnum


class ConsumableTypeEnum(str, Enum):
    vegetable = "VEGETABLE"
    fruit = "FRUIT"
    dairy = "DAIRY"
    other = "OTHER"


class ConsumableBase(BaseModel):
    name: str
    type: ConsumableEnum
    # image_path: str


class ConsumableCreate(ConsumableBase):
    pass


class Consumable(ConsumableBase):
    id: int
    image_path: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
