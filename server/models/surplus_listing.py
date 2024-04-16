from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Float, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class SurplusListing(Base):
    __tablename__ = "surplus_listings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    consumable_id = Column(Integer, ForeignKey('consumables.id'), nullable=False)
    price = Column(Float, nullable=False)
    booked = Column(Enum("1", "0"), default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    consumables = relationship("Consumables", back_populates="surplus_listings")