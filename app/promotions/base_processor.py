from abc import ABC, abstractmethod


class PromotionProcessor(ABC):

    @abstractmethod
    def apply(self, promotion, cart_items, amount, net_amount):
        """
        Apply a promotion.

        Returns:
            {
                "discount": float,
                "net_amount": float,
                "discounts": list
            }
        """
        pass