from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


class Register(BaseModel):
    name: str
    username: str
    email: str
    password: str
    image: str
    address: str
    phone: str
