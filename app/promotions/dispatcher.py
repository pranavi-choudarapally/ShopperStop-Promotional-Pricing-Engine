from app.promotions.flat_processor import FlatPromotionProcessor
from app.promotions.percentage_processor import PercentagePromotionProcessor
from app.promotions.category_processor import CategoryPromotionProcessor
from app.promotions.buy_x_get_y_processor import BuyXGetYProcessor
from app.promotions.time_processor import TimePromotionProcessor


class PromotionDispatcher:

    def __init__(self):

        self.processors = {

            "FLAT": FlatPromotionProcessor(),

            "PERCENTAGE": PercentagePromotionProcessor(),

            "CATEGORY": CategoryPromotionProcessor(),

            "BUY_X_GET_Y": BuyXGetYProcessor(),

            "TIME_BASED": TimePromotionProcessor()

        }

    def get_processor(self, promotion_type):

        return self.processors.get(
            promotion_type.upper()
        )

    def process(
        self,
        promotion,
        cart_items,
        amount,
        net_amount
    ):

        processor = self.get_processor(
            promotion.promotion_type
        )

        if processor is None:

            return {

                "discount": 0,

                "net_amount": net_amount,

                "discounts": []

            }

        return processor.apply(

            promotion,

            cart_items,

            amount,

            net_amount

        )