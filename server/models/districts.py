from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class Districts(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    province_id = Column(Integer, ForeignKey('provinces.id'))
    ecological_region = Column(String)

    province = relationship("Provinces", back_populates="districts")
    consumable_listing = relationship("ConsumableListing", back_populates="district")