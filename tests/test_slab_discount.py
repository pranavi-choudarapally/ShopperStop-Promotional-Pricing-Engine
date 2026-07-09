from app.discounts.slab_discount import calculate_slab_discount


def test_regular_customer_5000():

    result = calculate_slab_discount(5000, "REGULAR")

    assert result["discount"] == 0
    assert result["net_amount"] == 5000


def test_regular_customer_15000():

    result = calculate_slab_discount(15000, "REGULAR")

    assert result["discount"] == 1500
    assert result["net_amount"] == 13500


def test_premium_customer_15000():

    result = calculate_slab_discount(15000, "PREMIUM")

    assert result["discount"] == 3000
    assert result["net_amount"] == 12000