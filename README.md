# ShopperStop Promotional Pricing Engine

## Overview

The ShopperStop Promotional Pricing Engine is a RESTful backend application developed using FastAPI. It provides a flexible discount calculation engine that allows retailers to configure and apply different types of promotional discounts without changing application code.

The system supports customer-tier discounts, promotional campaigns, coupons, simulation of discounts, configurable business rules, and detailed bill calculation.

---

## Features

### Bill Calculation

- Progressive slab-based discount calculation
- Customer Tier support
    - Regular
    - Premium
- Detailed discount breakdown
- Savings summary
- Bill ID generation

### Promotion Management

- Create Promotion
- View Promotions
- Update Promotion
- Delete Promotion
- Activate Promotion
- Deactivate Promotion

### Coupon Management

- Create Coupon
- View Coupons
- Update Coupon
- Delete Coupon

### Customer Tier Management

- Create Customer Tier
- View Customer Tiers
- Update Customer Tier

### Simulation

- Preview discount calculation without generating a bill.

### Additional Discounts

- Promotional Discounts
- Coupon Discounts
- Happy Hour Discount
- Maximum Discount Cap

### Health Monitoring

- Health Check API
- Database Connectivity Check

### Logging

- Application Logs
- Bill Generation Logs

### Testing

- Unit Tests
- Integration Tests

---

## Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Pytest
- Docker

---

## Project Structure

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
│
├── logs
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── shopperstop.db
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd Shopper_Stop
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Running Tests

```bash
python -m pytest
```

---

## Available APIs

### Bills

POST

```
/api/v1/bills/calculate
```

---

### Promotions

POST

```
/api/v1/promotions
```

GET

```
/api/v1/promotions
```

PUT

```
/api/v1/promotions/{id}
```

DELETE

```
/api/v1/promotions/{id}
```

Activate

```
/api/v1/promotions/{id}/activate
```

Deactivate

```
/api/v1/promotions/{id}/deactivate
```

---

### Coupons

POST

```
/api/v1/coupons
```

GET

```
/api/v1/coupons
```

PUT

```
/api/v1/coupons/{id}
```

DELETE

```
/api/v1/coupons/{id}
```

---

### Customer Tier

POST

```
/api/v1/customer-tiers
```

GET

```
/api/v1/customer-tiers
```

PUT

```
/api/v1/customer-tiers/{id}
```

---

### Simulation

POST

```
/api/v1/promotions/simulate
```

---

### Health

GET

```
/api/v1/health
```

---

## Future Enhancements

- Category Discount
- Buy X Get Y Discount
- Configurable Discount Priority
- Feature Flags
- Caching
- Rate Limiting
- Audit Trail

---

## Author

Developed as part of the ShopperStop Backend Engineering Take Home Assignment.