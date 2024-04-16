from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base


class ResourceImages(Base):
    __tablename__ = "resource_images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    resource_id = Column(Integer, ForeignKey('resources.id'), nullable=False)
    image_path = Column(String)
    order = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    resource = relationship("Resources", back_populates="resource_images")
