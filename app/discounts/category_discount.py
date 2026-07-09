def calculate_category_discount(cart_items, promotions):

    total_discount = 0
    applied_discounts = []

    for promotion in promotions:

        if promotion.discount_type.upper() != "CATEGORY":
            continue

        if not promotion.category:
            continue

        for item in cart_items:

            if item.category.upper() == promotion.category.upper():

                item_total = item.quantity * item.unit_price

                discount = (
                    item_total * promotion.discount_value
                ) / 100

                total_discount += discount

                applied_discounts.append({

                    "type": "CATEGORY",

                    "name": promotion.name,

                    "category": promotion.category,

                    "discount_amount": round(discount, 2)

                })

    return total_discount, applied_discounts