from pydantic import BaseModel


class Quantity(BaseModel):
    quantity: float
