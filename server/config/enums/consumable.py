import enum
from sqlalchemy import Enum


class ConsumableEnum(enum.Enum):
    vegetable = "VEGETABLE"
    fruit = "FRUIT"
    dairy = "DAIRY"
    other = "OTHER"
