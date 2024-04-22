import enum
from sqlalchemy import Enum


class BookedEnum(enum.Enum):
    BOOKED = "BOOKED"
    NOT_BOOKED = "NOT_BOOKED"
