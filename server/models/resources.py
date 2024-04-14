from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class Resources(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, autoincrement=True)
    audience = Column(String, index=True)
    title = Column(String, index=True)
    description = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("User", back_populates="resources")
    resource_image = relationship("ResourceImage", back_populates="resource")