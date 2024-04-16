from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Float, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class SurplusListings(Base):
    __tablename__ = "surplus_listings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    consumable_id = Column(Integer, ForeignKey('consumables.id'), nullable=False)
    price = Column(Float, nullable=False)
    booked = Column(Enum("1", "0"), default=False, nullable=False)
    posted_date = Column(DateTime, default=datetime.now())

    consumable = relationship("Consumables", back_populates="surplus_listings")