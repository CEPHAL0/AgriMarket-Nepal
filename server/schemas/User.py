from pydantic import BaseModel
from enum import Enum
from config.enums.role import RoleEnum
from datetime import datetime


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
        orm_mode = True
