from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class MacroTypes(Base):
    __tablename__ = "macro_types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    consumable_macros = relationship("ConsumableMacros", back_populates="macro_type")