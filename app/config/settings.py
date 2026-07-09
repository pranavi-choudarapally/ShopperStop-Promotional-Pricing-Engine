import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CONFIG_PATH = os.path.join(
    BASE_DIR,
    "configs",
    "discount_config.json"
)


with open(CONFIG_PATH, "r") as file:
    DISCOUNT_CONFIG = json.load(file)