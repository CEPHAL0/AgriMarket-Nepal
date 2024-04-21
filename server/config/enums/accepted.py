import enum
from sqlalchemy import Enum


class AcceptedEnum(enum.Enum):
    ACCEPTED = "1"
    NOT_ACCEPTED = "0"
