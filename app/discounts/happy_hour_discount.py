from datetime import datetime

from app.config.settings import DISCOUNT_CONFIG


def calculate_happy_hour_discount(net_amount: float):

    config = DISCOUNT_CONFIG["happy_hour"]

    if not config["enabled"]:
        return 0

    current_time = datetime.now().strftime("%H:%M")

    if config["start"] <= current_time <= config["end"]:

        return net_amount * (config["discount"] / 100)

    return 0