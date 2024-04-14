from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class ResourceImage(Base):
    __tablename__ = "resource_image"

    id = Column(Integer, primary_key=True, autoincrement=True)
    resource_id = Column(Integer, ForeignKey('resources.id'))
    image_path_1 = Column(String)
    image_path_2 = Column(String)
    order = Column(Integer)

    resource = relationship("Resources", back_populates="resource_image")
