from pydantic import BaseModel


class CouponCreate(BaseModel):

    code: str

    discount_type: str

    discount_value: float

    minimum_purchase: float

    active: bool