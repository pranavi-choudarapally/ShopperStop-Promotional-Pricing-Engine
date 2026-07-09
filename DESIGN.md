# DESIGN DOCUMENT

# ShopperStop Promotional Pricing Engine

## 1. Introduction

The ShopperStop Promotional Pricing Engine is designed as a modular, extensible, and configuration-driven backend application. The primary objective is to provide a flexible discount engine that allows business teams to introduce or modify promotional rules without changing the application architecture.

The system follows a layered architecture that separates API handling, business logic, database operations, schemas, and discount calculations.

---

# 2. Architecture

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
      ┌────────────┼────────────┐
      ▼            ▼            ▼
 Slab Discount  Coupon      Promotion
      ▼            ▼            ▼
          Happy Hour Discount
                   │
                   ▼
             Database Layer
                   │
                   ▼
                SQLite
```

Each layer has a single responsibility, making the application easier to maintain and extend.

---

# 3. Folder Structure

```
app
│
├── config
│
├── configs
│
├── discounts
│
├── models
│
├── routers
│
├── schemas
│
├── services
│
├── utils
│
└── main.py
```

---

# 4. Responsibilities

## Routers

Handle HTTP requests and responses.

Examples:

- Promotion Router
- Coupon Router
- Customer Tier Router
- Simulation Router
- Health Router

---

## Services

Contain business logic.

Example:

BillService calculates the bill by coordinating different discount modules.

---

## Discount Engine

Acts as the central coordinator for all discount calculations.

Current supported discounts include:

- Progressive Slab Discount
- Promotion Discount
- Coupon Discount
- Happy Hour Discount
- Maximum Discount Cap

The design also supports future extensions such as Category Discount and Buy-X-Get-Y Discount.

---

## Schemas

Pydantic schemas are used for:

- Request validation
- Response validation
- Type checking

This prevents invalid API requests from reaching the business logic.

---

## Models

SQLAlchemy models represent database tables.

Current entities include:

- Promotion
- Coupon
- Customer Tier
- Bill

---

## Utils

Contains reusable utility modules.

Example:

Application Logger

---

# 5. Database Design

SQLite is used as the embedded database.

Reasons:

- Lightweight
- Zero configuration
- Easy to review
- Suitable for take-home assignments

---

# 6. Discount Flow

The discount engine processes discounts in the following order:

1. Customer Tier Slab Discount
2. Promotion Discount
3. Coupon Discount
4. Happy Hour Discount
5. Maximum Discount Cap

Each discount is applied independently and added to the final bill breakdown.

---

# 7. Design Decisions

### Why FastAPI?

- High performance
- Automatic Swagger documentation
- Built-in validation
- Easy REST API development

---

### Why SQLAlchemy?

- ORM support
- Database abstraction
- Easy migration to PostgreSQL or MySQL

---

### Why Pydantic?

- Strong validation
- Automatic serialization
- Cleaner API contracts

---

### Why Layered Architecture?

Separating routers, services, schemas, models, and discount modules improves maintainability, readability, testing, and future extensibility.

---

# 8. Extensibility

The system is designed to support additional discount types without major architectural changes.

Future enhancements include:

- Category Discount
- Buy X Get Y Discount
- Configurable Discount Priority
- Audit Trail
- Rate Limiting
- Feature Flags
- Caching

---

# 9. Error Handling

The application validates:

- Invalid request bodies
- Missing fields
- Incorrect data types
- Database connectivity

Meaningful HTTP responses are returned to clients.

---

# 10. Logging

Structured logging is implemented for:

- Bill generation
- Application events

Logs are stored inside the logs directory.

---

# 11. Testing Strategy

The application includes:

- Unit Tests
- Integration Tests

Core discount calculations and API endpoints are tested using Pytest and FastAPI TestClient.

---

# 12. Conclusion

The ShopperStop Promotional Pricing Engine provides a modular and extensible backend solution capable of supporting multiple promotional strategies. The layered architecture ensures maintainability while allowing future enhancements with minimal changes to the existing codebase.