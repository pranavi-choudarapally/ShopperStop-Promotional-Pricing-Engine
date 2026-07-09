from app.models.coupon import Coupon


def calculate_coupon_discount(db, coupon_code: str, amount: float, net_amount: float):

    total_discount = 0
    applied_coupon = []

    if not coupon_code:
        return total_discount, applied_coupon

    coupon = db.query(Coupon).filter(
        Coupon.code == coupon_code,
        Coupon.active == True
    ).first()

    if not coupon:
        return total_discount, applied_coupon

    if amount < coupon.minimum_purchase:
        return total_discount, applied_coupon

    discount = 0

    if coupon.discount_type.upper() == "FLAT":

        discount = coupon.discount_value

    elif coupon.discount_type.upper() == "PERCENTAGE":

        discount = (
            net_amount * coupon.discount_value
        ) / 100

    total_discount += discount

    applied_coupon.append({

        "type": "COUPON",

        "name": coupon.code,

        "discount_amount": round(discount, 2)

    })

    return total_discount, applied_coupon