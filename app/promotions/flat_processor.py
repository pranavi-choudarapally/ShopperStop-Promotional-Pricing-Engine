from app.promotions.base_processor import PromotionProcessor


class FlatPromotionProcessor(PromotionProcessor):

    def apply(self, promotion, cart_items, amount, net_amount):

        if amount < promotion.minimum_purchase:

            return {
                "discount": 0,
                "net_amount": net_amount,
                "discounts": []
            }

        discount = promotion.discount_value

        return {

            "discount": round(discount, 2),

            "net_amount": round(net_amount - discount, 2),

            "discounts": [
                {
                    "type": "PROMOTION",
                    "promotion_type": "FLAT",
                    "name": promotion.name,
                    "discount_amount": round(discount, 2)
                }
            ]
        }