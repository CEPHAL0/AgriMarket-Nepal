from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime


from config.database import Base
from config.enums.accepted import AcceptedEnum


class UserSurplusBookings(Base):
    __tablename__ = "user_surplus_bookings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    surplus_listing_id = Column(Integer, ForeignKey("surplus_listings.id"))
    booker_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    accepted = Column(Enum(AcceptedEnum), nullable=False)

    surplus_listing = relationship("SurplusListings", back_populates="bookings")

    booker = relationship(
        "Users", foreign_keys=[booker_id], back_populates="booker_bookings"
    )
