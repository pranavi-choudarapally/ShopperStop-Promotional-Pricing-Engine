from app.discounts.happy_hour_discount import calculate_happy_hour_discount


def test_happy_hour_discount():

    discount = calculate_happy_hour_discount(10500)

    assert discount >= 0