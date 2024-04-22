from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    String,
    ForeignKey,
    Float,
    DateTime,
    Enum,
)
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base
from config.enums.booked import BookedEnum


class SurplusListings(Base):
    __tablename__ = "surplus_listings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    consumable_id = Column(Integer, ForeignKey("consumables.id"), nullable=False)
    price = Column(Float, nullable=False)
    booked = Column(
        Enum(BookedEnum), default=BookedEnum.NOT_BOOKED.value, nullable=False
    )
    posted_date = Column(DateTime, default=datetime.now())
    farmer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    consumable = relationship("Consumables", back_populates="surplus_listings")

    bookings = relationship("UserSurplusBookings", back_populates="surplus_listing")

    farmer = relationship("Users", back_populates="surplus_listings")
