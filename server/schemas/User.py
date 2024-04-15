from pydantic import BaseModel
from enum import Enum


class RoleEnum(str, Enum):
    admin = "ADMIN"
    farmer = "FARMER"
    user = "USER"

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
        orm_mode = True
