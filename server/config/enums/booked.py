import enum
from sqlalchemy import Enum


class BookedEnum(enum.Enum):
    booked = "1"
    not_booked = "0"
