class DiscountContext:

    def __init__(
        self,
        amount,
        tier,
        cart_items,
        coupon_code,
        db,
        net_amount
    ):

        self.amount = amount

        self.tier = tier

        self.cart_items = cart_items

        self.coupon_code = coupon_code

        self.db = db

        self.net_amount = net_amount

        self.total_discount = 0

        self.discount_list = []