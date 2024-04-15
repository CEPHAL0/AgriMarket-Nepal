from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from config.database import Base

class Consumables(Base):
    __tablename__ = "consumables"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    type = Column(Enum('FRUIT', 'VEGETABLE', 'DAIRY', 'OTHER', name='consumable_types'), index=True)
    image_path = Column(String)

    consumable_listing = relationship("ConsumableListing", back_populates="consumables")
    bookings = relationship("UserSurplusBooking", back_populates="consumables")
    surplus_listing = relationship("SurplusListing", back_populates="consumables")
    prices = relationship("Prices", back_populates="consumables")
    consumable_macros = relationship("ConsumableMacros", back_populates="consumables")