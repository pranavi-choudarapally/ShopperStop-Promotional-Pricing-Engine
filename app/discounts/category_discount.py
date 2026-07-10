from app.config.settings import CATEGORY_DISCOUNTS


def calculate_category_discount(cart_items):

    total_discount = 0

    applied_discounts = []

    for item in cart_items:

        category = item.category

        if category in CATEGORY_DISCOUNTS:

            discount_rate = CATEGORY_DISCOUNTS[category]

            item_total = item.quantity * item.unit_price

            discount = (item_total * discount_rate) / 100

            total_discount += discount

            applied_discounts.append({
                "type": "CATEGORY",
                "name": f"{category} Category Discount",
                "category": category,
                "rate": f"{discount_rate}%",
                "discount_amount": round(discount, 2)
            })

    return round(total_discount, 2), applied_discounts