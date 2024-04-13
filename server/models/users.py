from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    image = Column(String)
    role = Column(String, index=True)
    address = Column(String)
    phone = Column(String, unique=True, index=True)
