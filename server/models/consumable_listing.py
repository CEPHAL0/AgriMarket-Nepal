from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class ConsumableListing(Base):
    __tablename__ = "consumable_listings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    consumable_id = Column(Integer, ForeignKey('consumables.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    district_id = Column(Integer, ForeignKey('districts.id'), nullable=False)
    price = Column(Float, nullable=False)
    posted_date = Column(DateTime, nullable=False)
    expiry_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    consumables = relationship("Consumables", back_populates="consumable_listing")
    user = relationship("User", back_populates="consumable_listing")
    district = relationship("Districts", back_populates="consumable_listing")