import enum
from sqlalchemy import Enum


class AudienceEnum(enum.Enum):
    farmer = "FARMER"
    user = "USER"
