from app.discounts.slab_discount import calculate_slab_discount
from app.discounts.category_discount import calculate_category_discount
from app.discounts.happy_hour_discount import calculate_happy_hour_discount

from app.models.coupon import Coupon
from app.models.promotion import Promotion

from app.config.settings import DISCOUNT_CONFIG

from app.promotions.dispatcher import PromotionDispatcher


def calculate_discount(
    amount: float,
    tier: str,
    cart_items,
    coupon_code: str,
    db
):

    # ---------------------------------------
    # Slab Discount
    # ---------------------------------------

    slab_result = calculate_slab_discount(amount, tier)

    total_discount = slab_result["discount"]
    net_amount = slab_result["net_amount"]

    discount_list = []

    discount_list.append({
        "type": "SLAB_BASED",
        "name": tier.title() + " Customer Discount",
        "discount_amount": slab_result["discount"],
        "breakdown": slab_result["breakdown"]
    })

    # ---------------------------------------
    # Category Discount
    # ---------------------------------------

    category_discount, category_discounts = calculate_category_discount(
        cart_items
    )

    if category_discount > 0:

        total_discount += category_discount

        net_amount -= category_discount

        discount_list.extend(category_discounts)

    # ---------------------------------------
    # Promotion Framework
    # ---------------------------------------

    dispatcher = PromotionDispatcher()

    promotions = db.query(Promotion).filter(
        Promotion.active == True
    ).all()

    for promotion in promotions:

        result = dispatcher.process(

            promotion=promotion,

            cart_items=cart_items,

            amount=amount,

            net_amount=net_amount

        )

        total_discount += result["discount"]

        net_amount = result["net_amount"]

        discount_list.extend(
            result["discounts"]
        )

    # ---------------------------------------
    # Coupon Discount
    # ---------------------------------------

    if coupon_code:

        coupon = db.query(Coupon).filter(
            Coupon.code == coupon_code,
            Coupon.active == True
        ).first()

        if coupon and amount >= coupon.minimum_purchase:

            coupon_discount = 0

            if coupon.discount_type.upper() == "FLAT":

                coupon_discount = coupon.discount_value

            elif coupon.discount_type.upper() == "PERCENTAGE":

                coupon_discount = (
                    net_amount * coupon.discount_value
                ) / 100

            total_discount += coupon_discount

            net_amount -= coupon_discount

            discount_list.append({

                "type": "COUPON",

                "name": coupon.code,

                "discount_amount": round(coupon_discount, 2)

            })

    # ---------------------------------------
    # Happy Hour Discount
    # ---------------------------------------

    happy_hour_discount = calculate_happy_hour_discount(
        net_amount
    )

    if happy_hour_discount > 0:

        total_discount += happy_hour_discount

        net_amount -= happy_hour_discount

        discount_list.append({

            "type": "HAPPY_HOUR",

            "name": "Happy Hour Discount",

            "discount_amount": round(
                happy_hour_discount,
                2
            )

        })

    # ---------------------------------------
    # Maximum Discount Cap
    # ---------------------------------------

    max_discount = (
        amount *
        DISCOUNT_CONFIG["maximum_discount_percentage"]
    ) / 100

    if total_discount > max_discount:

        total_discount = max_discount

        net_amount = amount - max_discount

    # ---------------------------------------
    # Final Response
    # ---------------------------------------

    return {

        "gross_amount": amount,

        "discount": round(
            total_discount,
            2
        ),

        "net_amount": round(
            net_amount,
            2
        ),

        "discounts_applied": discount_list

    }