from app.promotions.base_processor import PromotionProcessor


class PercentagePromotionProcessor(PromotionProcessor):

    def apply(self, promotion, cart_items, amount, net_amount):

        if amount < promotion.minimum_purchase:

            return {
                "discount": 0,
                "net_amount": net_amount,
                "discounts": []
            }

        discount = (
            net_amount * promotion.discount_value
        ) / 100

        return {

            "discount": round(discount, 2),

            "net_amount": round(net_amount - discount, 2),

            "discounts": [
                {
                    "type": "PROMOTION",
                    "promotion_type": "PERCENTAGE",
                    "name": promotion.name,
                    "discount_amount": round(discount, 2)
                }
            ]
        }