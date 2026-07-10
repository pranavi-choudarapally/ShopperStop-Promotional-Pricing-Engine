# ShopperStop Promotional Pricing Engine

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Docker](https://img.shields.io/badge/Docker-Supported-2496ED)
![Pytest](https://img.shields.io/badge/Testing-Pytest-success)

A configurable retail discount engine built using **FastAPI** that enables retailers to create and manage promotional campaigns, customer tier discounts, coupons, and bill calculations through REST APIs.

---

# Features

## Bill Calculation

- Progressive slab-based discount calculation
- Customer Tier support
  - Regular
  - Premium
- Detailed discount breakdown
- Savings summary
- Bill ID generation

---

## Promotion Management

- Create Promotion
- View Promotions
- Get Promotion by ID
- Update Promotion
- Delete Promotion
- Activate Promotion
- Deactivate Promotion

---

## Coupon Management

- Create Coupon
- View Coupons
- Update Coupon
- Delete Coupon

---

## Customer Tier Management

- Create Customer Tier
- View Customer Tiers
- Update Customer Tier

---

## Simulation

- Preview discount calculation without generating a bill

---

## Additional Discounts

- Promotional Discounts
- Coupon Discounts
- Category Discounts
- Happy Hour Discount
- Maximum Discount Cap

---

## Health Monitoring

- Health Check API
- Database Connectivity Check

---

## Logging

- Application Logs
- Bill Generation Logs

---

## Testing

- Unit Tests
- API Integration Tests

---

# Technology Stack

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Pytest
- Docker

---

# Project Structure

```
SHOPPER_STOP
│
├── app
│   ├── config
│   ├── configs
│   ├── discounts
│   ├── models
│   ├── routers
│   ├── schemas
│   ├── services
│   ├── utils
│   └── main.py
│
├── tests
├── logs
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── DESIGN.md
├── TESTING.md
├── ASSUMPTIONS.md
├── SUBMISSION.md
└── shopperstop.db
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/pranavi-choudarapally/ShopperStop-Promotional-Pricing-Engine.git
```

## Move into Project

```bash
cd ShopperStop-Promotional-Pricing-Engine
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
uvicorn app.main:app --reload
```

Application:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# Running Tests

```bash
python -m pytest
```

---

# Available APIs

## Bills

| Method | Endpoint |
|---------|----------|
| POST | `/api/v1/bills/calculate` |

---

## Promotions

| Method | Endpoint |
|---------|----------|
| POST | `/api/v1/promotions` |
| GET | `/api/v1/promotions` |
| GET | `/api/v1/promotions/{id}` |
| PUT | `/api/v1/promotions/{id}` |
| DELETE | `/api/v1/promotions/{id}` |
| POST | `/api/v1/promotions/{id}/activate` |
| POST | `/api/v1/promotions/{id}/deactivate` |

---

## Coupons

| Method | Endpoint |
|---------|----------|
| POST | `/api/v1/coupons` |
| GET | `/api/v1/coupons` |
| PUT | `/api/v1/coupons/{id}` |
| DELETE | `/api/v1/coupons/{id}` |

---

## Customer Tiers

| Method | Endpoint |
|---------|----------|
| POST | `/api/v1/customer-tiers` |
| GET | `/api/v1/customer-tiers` |
| PUT | `/api/v1/customer-tiers/{id}` |

---

## Simulation

| Method | Endpoint |
|---------|----------|
| POST | `/api/v1/promotions/simulate` |

---

## Health

| Method | Endpoint |
|---------|----------|
| GET | `/api/v1/health` |

---

# Example Response

```json
{
  "bill_id": "BILL-20260709212226",
  "customer_id": "CUST001",
  "gross_amount": 15000,
  "total_discount": 6000,
  "net_amount": 9000,
  "discounts_applied": [
    {
      "type": "SLAB_BASED",
      "discount_amount": 3000
    },
    {
      "type": "CATEGORY",
      "discount_amount": 2250
    },
    {
      "type": "PROMOTION",
      "discount_amount": 500
    },
    {
      "type": "COUPON",
      "discount_amount": 1000
    }
  ]
}
```

---

# Future Enhancements

- Buy X Get Y Discount
- Configurable Discount Priority
- Promotion Versioning
- Audit Trail
- Feature Flags
- Caching
- Rate Limiting
- Event-driven Promotion Lifecycle
- Rule Engine
- Multi-store Promotion Support

---

# Documentation

Additional documentation included in this repository:

- README.md
- DESIGN.md
- TESTING.md
- ASSUMPTIONS.md
- SUBMISSION.md

---

# Repository

GitHub Repository:

**https://github.com/pranavi-choudarapally/ShopperStop-Promotional-Pricing-Engine**

---

# Author

**Pranavi Choudarapally**

Developed as part of the ShopperStop Backend Engineering Take-Home Assignment using **FastAPI**, **SQLAlchemy**, **SQLite**, **Docker**, and **Pytest**.