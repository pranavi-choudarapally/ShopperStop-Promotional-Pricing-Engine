from app.services.discount_handlers import (
    apply_slab_discount,
    apply_category_discount,
    apply_promotion_discount,
    apply_coupon_discount,
    apply_happy_hour_discount
)


DISCOUNT_REGISTRY = {

    "SLAB": apply_slab_discount,

    "CATEGORY": apply_category_discount,

    "PROMOTION": apply_promotion_discount,

    "COUPON": apply_coupon_discount,

    "HAPPY_HOUR": apply_happy_hour_discount

}