from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    String,
    ForeignKey,
    Float,
    DateTime,
    Enum,
)
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class SoldConsumableQuantities(Base):
    __tablename__ = "sold_consumable_quantities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    consumable_id = Column(Integer, ForeignKey("consumables.id"), nullable=False)
    farmer_id = Column(Integer, ForeignKey("users.id"))
    quantity_sold = Column(Float, nullable=False)
    date_sold = Column(DateTime, default=datetime.now())

    consumable = relationship("Consumables", back_populates="sold_consumables")
    farmer = relationship("Users", back_populates="sold_consumable_quantities")

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
