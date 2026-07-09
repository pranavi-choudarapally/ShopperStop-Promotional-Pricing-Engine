from pydantic import BaseModel
from typing import List, Optional


class Customer(BaseModel):
    id: str
    tier: str


class CartItem(BaseModel):
    sku: str
    name: str
    category: str
    quantity: int
    unit_price: float


class Cart(BaseModel):
    items: List[CartItem]


class SimulationRequest(BaseModel):
    customer: Customer
    cart: Cart
    coupon_code: Optional[str] = None