import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# -------------------------
# Discount Configuration
# -------------------------

DISCOUNT_CONFIG_PATH = os.path.join(
    BASE_DIR,
    "configs",
    "discount_config.json"
)

with open(DISCOUNT_CONFIG_PATH, "r") as file:
    DISCOUNT_CONFIG = json.load(file)


# -------------------------
# Category Discount Configuration
# -------------------------

CATEGORY_CONFIG_PATH = os.path.join(
    BASE_DIR,
    "configs",
    "category_discount.json"
)

with open(CATEGORY_CONFIG_PATH, "r") as file:
    CATEGORY_DISCOUNTS = json.load(file)