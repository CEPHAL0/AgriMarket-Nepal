from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class UserSurplusBookings(Base):
    __tablename__ = "user_surplus_bookings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    consumable_id = Column(Integer, ForeignKey("consumables.id"))
    poster_id = Column(Integer, ForeignKey("users.id"))
    booker_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    consumables = relationship("Consumables", back_populates="bookings")

    poster = relationship("Users", foreign_keys=[poster_id], backref="poster_bookings")
    
    booker = relationship("Users", foreign_keys=[booker_id], backref="booker_bookings")
