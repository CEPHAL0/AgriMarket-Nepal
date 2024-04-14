from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class FarmerPerformance(Base):
    __tablename__ = "farmer_performance"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    performance = Column(Integer)

    user = relationship("User", back_populates="farmer_performance")