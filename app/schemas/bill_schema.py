from pydantic import BaseModel
from typing import List


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


class BillRequest(BaseModel):

    customer: Customer

    cart: Cart

    coupon_code: str | None = None