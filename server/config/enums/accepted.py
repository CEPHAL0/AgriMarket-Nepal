import enum
from sqlalchemy import Enum


class AcceptedEnum(enum.Enum):
    ACCEPTED = "ACCEPTED"
    NOT_ACCEPTED = "NOT_ACCEPTED"
