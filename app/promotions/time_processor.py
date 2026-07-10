from app.promotions.base_processor import PromotionProcessor


class TimePromotionProcessor(PromotionProcessor):

    def apply(self, promotion, cart_items, amount, net_amount):

        return {

            "discount": 0,

            "net_amount": net_amount,

            "discounts": []

        }