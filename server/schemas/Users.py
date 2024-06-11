from pydantic import BaseModel
from enum import Enum
from config.enums.role import RoleEnum
from datetime import datetime

from config.enums.role import RoleEnum


# class RoleEnum(str, Enum):
#     ADMIN = "ADMIN"
#     FARMER = "FARMER"
#     USER = "USER"


class UserBase(BaseModel):
    name: str
    username: str
    email: str
    image: str
    role: RoleEnum
    address: str
    phone: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserComplete(UserCreate):
    pass
