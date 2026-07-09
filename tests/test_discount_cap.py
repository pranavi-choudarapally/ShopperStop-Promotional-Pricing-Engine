from app.config.settings import DISCOUNT_CONFIG


def test_discount_cap():

    amount = 20000

    max_discount = (
        amount
        * DISCOUNT_CONFIG["maximum_discount_percentage"]
    ) / 100

    assert max_discount == 8000