from app.promotions.base_processor import PromotionProcessor


class BuyXGetYProcessor(PromotionProcessor):

    def apply(self, promotion, cart_items, amount, net_amount):

        if promotion.buy_quantity is None:
            return {
                "discount": 0,
                "net_amount": net_amount,
                "discounts": []
            }

        if promotion.free_quantity is None:
            return {
                "discount": 0,
                "net_amount": net_amount,
                "discounts": []
            }

        total_discount = 0

        discount_list = []

        for item in cart_items:

            # SKU based promotion

            if promotion.applicable_sku:

                if item.sku != promotion.applicable_sku:
                    continue

            # Category based promotion

            elif promotion.category:

                if item.category.upper() != promotion.category.upper():
                    continue

            else:
                continue

            eligible_free_items = (
                item.quantity // promotion.buy_quantity
            ) * promotion.free_quantity

            if eligible_free_items <= 0:
                continue

            discount = eligible_free_items * item.unit_price

            total_discount += discount

            discount_list.append({

                "type": "BUY_X_GET_Y",

                "name": promotion.name,

                "buy_quantity": promotion.buy_quantity,

                "free_quantity": promotion.free_quantity,

                "free_items": eligible_free_items,

                "discount_amount": round(discount, 2)

            })

        return {

            "discount": round(total_discount, 2),

            "net_amount": round(net_amount - total_discount, 2),

            "discounts": discount_list

        }