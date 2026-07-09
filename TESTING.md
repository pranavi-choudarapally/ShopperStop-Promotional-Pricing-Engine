# TESTING DOCUMENT

# ShopperStop Promotional Pricing Engine

## Overview

The application has been tested using unit tests and integration tests to ensure correctness of the discount calculation engine and REST APIs.

The tests are written using **Pytest** and **FastAPI TestClient**.

---

# Running Tests

Activate the virtual environment.

Windows

```bash
venv\Scripts\activate
```

Run all tests.

```bash
python -m pytest
```

---

# Test Coverage

The following modules are tested.

## Unit Tests

### Slab Discount

File:

```
tests/test_slab_discount.py
```

Scenarios covered:

- Regular Customer ₹5,000
- Regular Customer ₹15,000
- Premium Customer ₹15,000

---

### Coupon Discount

File:

```
tests/test_coupon_discount.py
```

Scenarios covered:

- Valid Coupon
- Coupon Discount Applied

---

### Happy Hour Discount

File:

```
tests/test_happy_hour_discount.py
```

Scenario covered:

- Happy Hour Discount Calculation

---

### Maximum Discount Cap

File:

```
tests/test_discount_cap.py
```

Scenario covered:

- Maximum Discount Limit

---

# Integration Tests

## Health API

File

```
tests/test_health_api.py
```

Verifies

- Status Code
- Database Connectivity
- Health Response

---

## Bill API

File

```
tests/test_bill_api.py
```

Verifies

- Bill Calculation
- Discount Breakdown
- Customer Details
- Bill Generation

---

# Test Result

Current Result

```
8 Tests Passed
```

---

# Validation

The application has been manually verified using Swagger UI.

Verified APIs

- Bill API
- Promotion APIs
- Coupon APIs
- Customer Tier APIs
- Simulation API
- Health API

---

# Conclusion

The testing strategy combines unit testing for business logic and integration testing for REST APIs, ensuring that the core pricing engine behaves correctly across different scenarios.