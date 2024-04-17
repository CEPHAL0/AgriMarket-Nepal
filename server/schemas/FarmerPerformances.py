from pydantic import BaseModel
from datetime import datetime


class FarmerPerformanceBase(BaseModel):
    farmer_id: int
    performance: int


class FarmerPerformanceCreate(FarmerPerformanceBase):
    pass


class FarmerPerformance(FarmerPerformanceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
