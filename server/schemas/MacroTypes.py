from pydantic import BaseModel
from datetime import datetime


class MacroTypeBase(BaseModel):
    name: str

class MacroTypeCreate(MacroTypeBase):
    pass


class MacroType(MacroTypeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True