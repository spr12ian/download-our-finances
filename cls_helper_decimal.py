from decimal import Decimal, getcontext, ROUND_HALF_UP


def round_money(value) -> Decimal:
    """Ensure all money values are rounded correctly to 2 decimal places."""
    return value.quantize(Decimal("0.01"))


# Set the global rounding mode
getcontext().rounding = ROUND_HALF_UP

# Example calculations
amount = Decimal("12.34567")
rounded_amount = round_money(amount)  # Uses ROUND_HALF_UP by default

print(rounded_amount)  # Output: 12.35
