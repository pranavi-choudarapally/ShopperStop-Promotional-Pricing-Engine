from app.discounts.slab_discount import calculate_slab_discount
from app.discounts.category_discount import calculate_category_discount
from app.discounts.happy_hour_discount import calculate_happy_hour_discount

from app.models.coupon import Coupon
from app.models.promotion import Promotion

from app.promotions.dispatcher import PromotionDispatcher


# --------------------------------------------------
# Slab Discount Handler
# --------------------------------------------------

def apply_slab_discount(amount, tier):

    slab_result = calculate_slab_discount(amount, tier)

    return {

        "discount": slab_result["discount"],

        "net_amount": slab_result["net_amount"],

        "discounts": [

            {

                "type": "SLAB_BASED",

                "name": tier.title() + " Customer Discount",

                "discount_amount": slab_result["discount"],

                "breakdown": slab_result["breakdown"]

            }

        ]

    }


# --------------------------------------------------
# Category Discount Handler
# --------------------------------------------------

def apply_category_discount(cart_items):

    category_discount, category_discounts = calculate_category_discount(
        cart_items
    )

    return {

        "discount": category_discount,

        "discounts": category_discounts

    }


# --------------------------------------------------
# Promotion Discount Handler
# --------------------------------------------------

def apply_promotion_discount(
    amount,
    net_amount,
    cart_items,
    db
):

    dispatcher = PromotionDispatcher()

    total_discount = 0

    applied_discounts = []

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

        applied_discounts.extend(
            result["discounts"]
        )

    return {

        "discount": round(total_discount, 2),

        "net_amount": round(net_amount, 2),

        "discounts": applied_discounts

    }


# --------------------------------------------------
# Coupon Discount Handler
# --------------------------------------------------

def apply_coupon_discount(
    coupon_code,
    amount,
    net_amount,
    db
):

    if not coupon_code:

        return {

            "discount": 0,

            "net_amount": net_amount,

            "discounts": []

        }

    coupon = db.query(Coupon).filter(

        Coupon.code == coupon_code,

        Coupon.active == True

    ).first()

    if not coupon:

        return {

            "discount": 0,

            "net_amount": net_amount,

            "discounts": []

        }

    if amount < coupon.minimum_purchase:

        return {

            "discount": 0,

            "net_amount": net_amount,

            "discounts": []

        }

    coupon_discount = 0

    if coupon.discount_type.upper() == "FLAT":

        coupon_discount = coupon.discount_value

    elif coupon.discount_type.upper() == "PERCENTAGE":

        coupon_discount = (
            net_amount * coupon.discount_value
        ) / 100

    return {

        "discount": round(coupon_discount, 2),

        "net_amount": round(
            net_amount - coupon_discount,
            2
        ),

        "discounts": [

            {

                "type": "COUPON",

                "name": coupon.code,

                "discount_amount": round(
                    coupon_discount,
                    2
                )

            }

        ]

    }


# --------------------------------------------------
# Happy Hour Discount Handler
# --------------------------------------------------

def apply_happy_hour_discount(net_amount):

    happy_hour_discount = calculate_happy_hour_discount(
        net_amount
    )

    if happy_hour_discount <= 0:

        return {

            "discount": 0,

            "net_amount": net_amount,

            "discounts": []

        }

    return {

        "discount": round(
            happy_hour_discount,
            2
        ),

        "net_amount": round(
            net_amount - happy_hour_discount,
            2
        ),

        "discounts": [

            {

                "type": "HAPPY_HOUR",

                "name": "Happy Hour Discount",

                "discount_amount": round(
                    happy_hour_discount,
                    2
                )

            }

        ]

    }