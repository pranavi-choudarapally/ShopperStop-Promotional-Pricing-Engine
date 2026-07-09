from app.discounts.coupon_discount import calculate_coupon_discount


class MockCoupon:
    def __init__(self):
        self.code = "SAVE1000"
        self.active = True
        self.minimum_purchase = 5000
        self.discount_type = "FLAT"
        self.discount_value = 1000


class MockQuery:
    def filter(self, *args):
        return self

    def first(self):
        return MockCoupon()


class MockDB:
    def query(self, model):
        return MockQuery()


def test_coupon_discount():

    db = MockDB()

    discount, applied = calculate_coupon_discount(
        db,
        "SAVE1000",
        15000,
        12000
    )

    assert discount == 1000
    assert applied[0]["type"] == "COUPON"