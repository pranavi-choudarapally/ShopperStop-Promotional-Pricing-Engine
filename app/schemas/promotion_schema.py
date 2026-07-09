from pydantic import BaseModel


class PromotionCreate(BaseModel):

    name: str

    # FLAT / PERCENTAGE / CATEGORY
    discount_type: str

    discount_value: float

    minimum_purchase: float

    category: str | None = None

    active: bool = False