from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class SurplusListing(Base):
    __tablename__ = "surplus_listing"

    id = Column(Integer, primary_key=True, autoincrement=True)
    consumable_id = Column(Integer, ForeignKey('consumables.id'))
    price = Column(Float)
    booked = Column(Boolean, default=False)
    posted_date = Column(DateTime, default=datetime.now())

    consumables = relationship("Consumables", back_populates="surplus_listing")