import enum
from sqlalchemy import Enum


class ConsumableEnum(enum.Enum):
    VEGETABLE = "VEGETABLE"
    FRUIT = "FRUIT"
    DAIRY = "DAIRY"
    OTHER = "OTHER"
