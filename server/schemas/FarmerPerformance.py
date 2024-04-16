from pydantic import BaseModel
from datetime import datetime


class FarmerPerformancesBase(BaseModel):
    farmer_id: int
    performance: int


class FarmerPerformanceCreate(FarmerPerformancesBase):
    pass


class FarmerPerformances(FarmerPerformancesBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True