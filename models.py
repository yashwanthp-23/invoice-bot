# app/models.py
from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    name: str
    quantity: int
    price: float

class Invoice(BaseModel):
    user_id: str
    items: List[OrderItem]
    total: float
    date: str
