from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class Districts(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    province_id = Column(Integer, ForeignKey('provinces.id'))
    ecological_region = Column(String)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    province = relationship("Provinces", back_populates="districts")

    consumable_listings = relationship("ConsumableListings", back_populates="district")