from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import relationship
from . import UserSurplusBooking

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

    farmer_performance = relationship("FarmerPerformance", back_populates="user")
    resources = relationship("Resources", back_populates="author")
    consumable_listing = relationship("ConsumableListing", back_populates="user")
    poster_bookings = relationship("UserSurplusBooking", foreign_keys=[UserSurplusBooking.poster_id], back_populates="poster")
    booker_bookings = relationship("UserSurplusBooking", foreign_keys=[UserSurplusBooking.booker_id], back_populates="booker")