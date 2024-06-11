from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    String,
    ForeignKey,
    Float,
    Enum,
    DateTime,
)
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

    consumable_listings = relationship(
        "ConsumableListings", back_populates="consumable"
    )

    surplus_listings = relationship("SurplusListings", back_populates="consumable")

    sold_consumables = relationship(
        "SoldConsumableQuantities", back_populates="consumable"
    )

    prices = relationship("Prices", back_populates="consumable")

    consumable_macros = relationship("ConsumableMacros", back_populates="consumable")
