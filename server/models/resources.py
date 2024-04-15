from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class Resources(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, autoincrement=True)
    audience = Column(Enum('FARMER', 'USER'), index=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    author = relationship("User", back_populates="resources")
    resource_image = relationship("ResourceImage", back_populates="resource")