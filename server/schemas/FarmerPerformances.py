from pydantic import BaseModel
from datetime import datetime
from schemas.Users import User


class FarmerPerformanceBase(BaseModel):
    farmer_id: int
    performance: int


class FarmerPerformanceCreate(FarmerPerformanceBase):
    pass


class FarmerPerformance(FarmerPerformanceBase):
    id: int
    farmer: User
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
