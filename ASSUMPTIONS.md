# ASSUMPTIONS

# ShopperStop Promotional Pricing Engine

During the implementation of this assignment, the following assumptions were made.

---

## 1. Customer Tier

Only two customer tiers are currently supported.

- REGULAR
- PREMIUM

Additional tiers can be added through the Customer Tier API.

---

## 2. Promotion Stacking

Multiple promotions are allowed to stack unless restricted by the maximum discount cap.

The discount order is currently:

1. Slab Discount
2. Promotion Discount
3. Coupon Discount
4. Happy Hour Discount
5. Maximum Discount Cap

---

## 3. Coupons

Only one coupon can be applied per bill.

If the coupon is inactive or the minimum purchase amount is not satisfied, it is ignored.

---

## 4. Database

SQLite is used because the assignment requested an embedded database without requiring external setup.

The application can be migrated to PostgreSQL or MySQL with minimal changes.

---

## 5. Promotion Configuration

Current implementation supports:

- Flat Discount
- Percentage Discount

Future versions can support:

- Category Discount
- Buy X Get Y Discount
- Time-Based Promotions
- Store Specific Promotions

---

## 6. Happy Hour

Happy Hour discount is currently implemented as an additional configurable percentage discount.

The timing logic can be extended using configurable business rules.

---

## 7. Discount Cap

A maximum discount percentage is enforced using configuration settings.

If calculated discounts exceed the cap, the final discount is limited accordingly.

---

## 8. Bill Calculation

Bill calculation is stateless.

Every API request performs a fresh calculation without depending on previous requests.

---

## 9. Authentication

Authentication and authorization are outside the scope of this assignment.

All APIs are currently open for demonstration purposes.

---

## 10. Future Improvements

The architecture has been designed to allow future implementation of:

- Category Discount
- Buy X Get Y Discount
- Configurable Discount Priority
- Audit Logging
- Feature Flags
- Rate Limiting
- Caching