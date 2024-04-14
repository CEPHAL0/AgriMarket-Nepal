from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class ConsumableListing(Base):
    __tablename__ = "consumable_listing"

    id = Column(Integer, primary_key=True, autoincrement=True)
    consumable_id = Column(Integer, ForeignKey('consumables.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    price = Column(Float) 
    posted_date = Column(DateTime, default=datetime.now())
    district_id = Column(Integer, ForeignKey('districts.id'))

    consumables = relationship("Consumables", back_populates="consumable_listing")
    user = relationship("User", back_populates="consumable_listing")
    district = relationship("Districts", back_populates="consumable_listing")