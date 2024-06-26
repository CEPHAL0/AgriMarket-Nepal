from sqlalchemy import Column, Boolean, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from config.enums.role import RoleEnum

from models.index import user_surplus_bookings

from config.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    image = Column(String)
    role = Column(Enum(RoleEnum), index=True)
    address = Column(String)
    phone = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    farmer_performances = relationship("FarmerPerformances", back_populates="farmer")

    resources = relationship("Resources", back_populates="author")

    consumable_listings = relationship("ConsumableListings", back_populates="user")

    booker_bookings = relationship(
        "UserSurplusBookings",
        foreign_keys=[user_surplus_bookings.UserSurplusBookings.booker_id],
        back_populates="booker",
    )

    sold_consumable_quantities = relationship(
        "SoldConsumableQuantities", back_populates="farmer"
    )

    surplus_listings = relationship("SurplusListings", back_populates="farmer")

    # poster_bookings = relationship("UserSurplusBooking", foreign_keys=[UserSurplusBooking.poster_id], back_populates="poster")

    # booker_bookings = relationship("UserSurplusBooking", foreign_keys=[UserSurplusBooking.booker_id], back_populates="booker")
