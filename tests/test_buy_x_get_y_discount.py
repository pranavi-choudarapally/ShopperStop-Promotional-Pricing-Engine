from types import SimpleNamespace

from app.promotions.buy_x_get_y_processor import BuyXGetYProcessor


def test_buy_2_get_1_same_sku():

    promotion = SimpleNamespace(

        name="Buy 2 Get 1",

        buy_quantity=2,

        free_quantity=1,

        applicable_sku="SHIRT001",

        category=None

    )

    cart_items = [

        SimpleNamespace(

            sku="SHIRT001",

            category="Clothing",

            quantity=7,

            unit_price=1000

        )

    ]

    processor = BuyXGetYProcessor()

    result = processor.apply(

        promotion,

        cart_items,

        amount=7000,

        net_amount=7000

    )

    assert result["discount"] == 3000

    assert result["net_amount"] == 4000