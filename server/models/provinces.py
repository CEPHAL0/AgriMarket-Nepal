from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class Provinces(Base):
    __tablename__ = "provinces"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    districts = relationship("Districts", back_populates="province")