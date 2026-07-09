from app.models.promotion import Promotion


def calculate_promotion_discount(db, amount: float, net_amount: float):

    total_discount = 0
    applied_promotions = []

    promotions = db.query(Promotion).filter(
        Promotion.active == True
    ).all()

    for promotion in promotions:

        if promotion.discount_type.upper() == "CATEGORY":
            # Category discounts will be handled separately
            continue

        if amount < promotion.minimum_purchase:
            continue

        discount = 0

        if promotion.discount_type.upper() == "FLAT":

            discount = promotion.discount_value

        elif promotion.discount_type.upper() == "PERCENTAGE":

            discount = (
                net_amount * promotion.discount_value
            ) / 100

        if discount > 0:

            total_discount += discount

            applied_promotions.append({

                "type": "PROMOTION",

                "name": promotion.name,

                "discount_amount": round(discount, 2)

            })

    return total_discount, applied_promotions