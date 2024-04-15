from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base

class Consumables(Base):
    __tablename__ = "consumables"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    type = Column(Enum('FRUIT', 'VEGETABLE', 'DAIRY', 'OTHER', name='consumable_types'), index=True, nullable=False)
    image_path = Column(String, unique=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)