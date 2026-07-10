from datetime import datetime
from pydantic import BaseModel


class PromotionCreate(BaseModel):

    # -----------------------------
    # Basic Information
    # -----------------------------

    name: str

    description: str | None = None

    promotion_type: str

    discount_type: str

    discount_value: float

    minimum_purchase: float = 0

    # -----------------------------
    # Category
    # -----------------------------

    category: str | None = None

    # -----------------------------
    # Buy X Get Y
    # -----------------------------

    buy_quantity: int | None = None

    free_quantity: int | None = None

    # -----------------------------
    # Product & Store
    # -----------------------------

    applicable_sku: str | None = None

    applicable_store: str | None = None

    # -----------------------------
    # Scheduling
    # -----------------------------

    start_time: datetime | None = None

    end_time: datetime | None = None

    # -----------------------------
    # Rule Engine
    # -----------------------------

    priority: int = 1

    stackable: bool = True

    usage_limit: int | None = None

    # -----------------------------
    # Status
    # -----------------------------

    active: bool = True


class PromotionResponse(PromotionCreate):

    id: int

    version: int

    created_at: datetime

    updated_at: datetime

    class Config:
        from_attributes = True