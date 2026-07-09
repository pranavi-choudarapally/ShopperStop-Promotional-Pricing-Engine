# ShopperStop Promotional Pricing Engine

## Overview

The ShopperStop Promotional Pricing Engine is a RESTful backend application developed using FastAPI. It provides a flexible and extensible discount calculation engine that allows retailers to configure and apply different promotional discounts without changing application code.

The system supports customer-tier discounts, promotional campaigns, coupons, simulation of discounts, configurable business rules, health monitoring, logging, and detailed bill calculation.

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

- Preview discount calculation without generating a bill

### Additional Discounts

- Promotional Discounts
- Coupon Discounts
- Happy Hour Discount
- Maximum Discount Cap

### Configuration

- Configurable discount settings using JSON
- Customer Tier configuration
- Maximum Discount Cap configuration

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
- SQLite (Embedded Database)
- Pydantic
- Uvicorn
- Pytest
- Docker

---

## Architecture

The application follows a layered architecture.

```
Client
   │
   ▼
FastAPI Routers
   │
   ▼
Service Layer
   │
   ▼
Discount Engine
   │
   ▼
SQLite Database
```

This architecture separates routing, business logic, validation, and persistence, making the application modular, maintainable, and easy to extend.

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
├── logs
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── shopperstop.db
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/pranavi-choudarapally/ShopperStop-Promotional-Pricing-Engine.git
```

Move into the project.

```bash
cd ShopperStop-Promotional-Pricing-Engine
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

Install dependencies.

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

OpenAPI JSON

```
http://127.0.0.1:8000/openapi.json
```

---

## Running Tests

Run all tests.

```bash
python -m pytest
```

### Current Test Status

```
8 Tests Passed
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

- Category-based Discount Engine
- Buy X Get Y Discount Engine
- Configurable Discount Priority
- Promotion Versioning
- Audit Trail
- Redis Caching
- Feature Flags
- Rate Limiting

---

## Author

Developed by **Pranavi Choudarapally** as part of the ShopperStop Backend Engineering Take Home Assignment.

---

## License

This project was developed for educational and evaluation purposes as part of the ShopperStop Backend Engineering Take Home Assignment.