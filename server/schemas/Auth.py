from pydantic import BaseModel
from fastapi import File, UploadFile
from typing import Optional


class Login(BaseModel):
    username: str
    password: str


class Register(BaseModel):
    name: str
    username: str
    email: str
    password: str
    # image: Optional[str] = None
    image: str
    # image: Optional[UploadFile] = None
    address: str
    phone: str
