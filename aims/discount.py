def calculate_discount(total, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")

    return total * (100 - percent) / 100