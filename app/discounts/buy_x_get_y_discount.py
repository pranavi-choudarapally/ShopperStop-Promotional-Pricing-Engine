def calculate_buy_x_get_y_discount(cart_items):

    total_discount = 0
    applied_discounts = []

    for item in cart_items:

        # Example Rule:
        # Buy 2 Shirts, Get 1 Shirt Free

        if item.category.upper() == "CLOTHING":

            if item.quantity >= 3:

                free_items = item.quantity // 3

                discount = free_items * item.unit_price

                total_discount += discount

                applied_discounts.append({

                    "type": "BUY_X_GET_Y",

                    "name": "Buy 2 Get 1 Free",

                    "item": item.name,

                    "free_items": free_items,

                    "discount_amount": round(discount, 2)

                })

    return total_discount, applied_discounts