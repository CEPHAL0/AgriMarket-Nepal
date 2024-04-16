from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from config.enums.consumable import ConsumableEnum

from config.database import Base

class Consumables(Base):
    __tablename__ = "consumables"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    type = Column(Enum(ConsumableEnum), index=True, nullable=False)
    image_path = Column(String, unique=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    consumable_listings = relationship("ConsumableListing", back_populates="consumables")
    bookings = relationship("UserSurplusBooking", back_populates="consumables")
    surplus_listings = relationship("SurplusListing", back_populates="consumables")
    prices = relationship("Prices", back_populates="consumables")
    consumable_macros = relationship("ConsumableMacros", back_populates="consumables")