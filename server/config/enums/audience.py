import enum
from sqlalchemy import Enum


class AudienceEnum(enum.Enum):
    FARMER = "FARMER"
    USER = "USER"
