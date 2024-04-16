from pydantic import BaseModel
from datetime import datetime


class MacroTypesBase(BaseModel):
    name: str

class MacroTypeCreate(MacroTypesBase):
    pass


class MacroTypes(MacroTypesBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True