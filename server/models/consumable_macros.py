from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class ConsumableMacros(Base):
    __tablename__ = "consumable_macros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    consumable_id = Column(Integer, ForeignKey('consumables.id'))
    macro_id = Column(Integer, ForeignKey('macro_types.id'))
    quantity = Column(Float)

    consumables = relationship("Consumables", back_populates="consumable_macros")
    macro = relationship("MacroTypes", back_populates="consumable_macros")