from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class ConsumableMacros(Base):
    __tablename__ = "consumable_macros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    consumable_id = Column(Integer, ForeignKey('consumables.id'), nullable=False)
    macro_type_id = Column(Integer, ForeignKey('macro_types.id'), nullable=False)
    quantity = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    consumable = relationship("Consumables", back_populates="consumable_macros")
    
    macro_type = relationship("MacroTypes", back_populates="consumable_macros")