from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class UserSurplusBooking(Base):
    __tablename__ = "user_surplus_booking"

    id = Column(Integer, primary_key=True, autoincrement=True)
    consumable_id = Column(Integer, ForeignKey('consumables.id'))
    poster_id = Column(Integer, ForeignKey('users.id'))
    booker_id = Column(Integer, ForeignKey('users.id'))

    consumables = relationship("Consumables", back_populates="bookings")
    poster = relationship("User", foreign_keys=[poster_id], backref="poster_bookings")
    booker = relationship("User", foreign_keys=[booker_id], backref="booker_bookings")