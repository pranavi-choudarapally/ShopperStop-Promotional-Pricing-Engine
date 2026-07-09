from app.config.settings import DISCOUNT_CONFIG


def calculate_slab_discount(amount: float, tier: str):

    tier = tier.upper()

    slabs = DISCOUNT_CONFIG["customer_tiers"][tier]["slabs"]

    discount = 0
    breakdown = []

    for slab in slabs:

        minimum = slab["min"]
        maximum = slab["max"]
        rate = slab["discount"]

        # Amount that belongs to this slab
        if amount <= minimum:
            continue

        if maximum is None:
            slab_amount = amount - minimum
        else:
            slab_amount = min(amount, maximum) - minimum

        if slab_amount <= 0:
            continue

        slab_discount = slab_amount * (rate / 100)

        discount += slab_discount

        if maximum is None:
            slab_name = f"{minimum + 1}+"
        else:
            slab_name = f"{minimum}-{maximum}"

        breakdown.append({
            "slab": slab_name,
            "amount": slab_amount,
            "rate": f"{rate}%",
            "discount": slab_discount
        })

    return {
        "gross_amount": amount,
        "discount": discount,
        "net_amount": amount - discount,
        "breakdown": breakdown
    }