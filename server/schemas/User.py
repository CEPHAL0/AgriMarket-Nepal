from pydantic import BaseModel
from enum import Enum

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

    class Config:
        from_attributes = True
