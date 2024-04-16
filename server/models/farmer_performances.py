from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class FarmerPerformances(Base):
    __tablename__ = "farmer_performances"

    id = Column(Integer, primary_key=True, autoincrement=True)
    farmer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    performance = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    farmer = relationship("Users", back_populates="farmer_performances")
