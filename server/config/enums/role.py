import enum
from sqlalchemy import Enum


class RoleEnum(enum.Enum):
    ADMIN = "ADMIN"
    FARMER = "FARMER"
    USER = "USER"
