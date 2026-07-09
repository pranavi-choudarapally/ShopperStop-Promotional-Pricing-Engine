from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_calculate_bill():

    payload = {
        "customer": {
            "id": "CUST001",
            "tier": "PREMIUM"
        },
        "cart": {
            "items": [
                {
                    "sku": "SKU101",
                    "name": "Laptop",
                    "category": "Electronics",
                    "quantity": 1,
                    "unit_price": 15000
                }
            ]
        },
        "coupon_code": "SAVE1000"
    }

    response = client.post(
        "/api/v1/bills/calculate",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["customer_id"] == "CUST001"
    assert data["gross_amount"] == 15000
    assert "bill_id" in data
    assert "discounts_applied" in data