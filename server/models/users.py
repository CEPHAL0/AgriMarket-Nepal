from sqlalchemy import Column, Boolean, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

# from .user_surplus_booking import UserSurplusBooking

from config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    image = Column(String)
    role = Column(Enum('ADMIN', 'FARMER', 'USER', name='consumable_types'), index=True)
    address = Column(String)
    phone = Column(String, unique=True, index=True)
    profession = Column(String, unique=False, index=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    farmer_performance = relationship("FarmerPerformance", back_populates="user")
    resources = relationship("Resources", back_populates="author")
    consumable_listing = relationship("ConsumableListing", back_populates="user")
    # poster_bookings = relationship("UserSurplusBooking", foreign_keys=[UserSurplusBooking.poster_id], back_populates="poster")
    # booker_bookings = relationship("UserSurplusBooking", foreign_keys=[UserSurplusBooking.booker_id], back_populates="booker")
