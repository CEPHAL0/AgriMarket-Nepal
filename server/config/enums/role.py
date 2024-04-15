import enum
from sqlalchemy import Enum


class RoleEnum(enum.Enum):
    admin = "ADMIN"
    farmer = "FARMER"
    user = "USER"
