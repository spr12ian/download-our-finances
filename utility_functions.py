import locale
import math
import re
from cls_helper_date_time import DateTimeHelper
from cls_helper_log import LogHelper
from decimal import Decimal, InvalidOperation

l = LogHelper("utility_functions")
l.set_level_debug()
l.debug(__file__)


def all_conditions_are_false(conditions: list) -> bool:
    if not all_items_are_boolean(conditions):
        raise ValueError("Not all conditions are boolean")

    return not any(conditions)


def all_items_are_boolean(lst: list) -> bool:
    return all(isinstance(item, bool) for item in lst)


def crop(string: str, excess: str) -> str:
    excess_length = len(excess)
    if string[-excess_length:] == excess:
        string = string[:-excess_length]
    return string


def format_as_gbp(amount: float, field_width: int = 0) -> str:
    """
    Format a float as GBP.
    """
    # Set the locale to GBP
    locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")

    # Format the float as currency
    formatted_amount = locale.currency(amount, grouping=True)

    # Right justify the formatted amount within the specified field width
    return f"{formatted_amount:>{field_width}}"


def format_as_gbp_or_blank(amount: float) -> str:
    """
    Format a float as GBP or blank if zero.
    """

    if abs(amount) < 0.01:
        return ""
    else:
        # Format the float as currency
        return format_as_gbp(amount)


import re


def remove_non_numeric(string: str) -> str:
    """
    Remove all characters from a string except digits or decimal points.
    """
    return re.sub(r"[^\d.]", "", string)


def round_down(number: float) -> int:
    return math.floor(number)


def round_up(number: float) -> int:
    return math.ceil(number)


# Function to convert currency/percent strings to float
def string_to_financial(string: str) -> Decimal:
    if string.strip() == "":  # Check if the string is empty or whitespace
        return Decimal("0.00")

    # Remove any currency symbols and thousand separators
    string = re.sub(r"[^\d.,%]", "", string)
    string = string.replace(",", "")

    # Check if the string has a percentage symbol
    if "%" in string:
        string = string.replace("%", "")
        try:
            return Decimal(string) / Decimal("100")
        except InvalidOperation:
            return Decimal("0.00")

    try:
        return Decimal(string)
    except InvalidOperation:
        return Decimal("0.00")


# Function to convert currency/percent strings to float
def string_to_float(string) -> float:
    if string.strip() == "":  # Check if the string is empty or whitespace
        return 0.0

    # Remove any currency symbols and thousand separators
    string = re.sub(r"[^\d.,%]", "", string)
    string = string.replace(",", "")

    # Check if the string has a percentage symbol
    if "%" in string:
        string = string.replace("%", "")
        return float(string) / 100

    return float(string)


def sum_values(lst: list) -> float:
    l.debug("sum_values")
    l.debug(lst)
    total = 0
    for value in lst:
        total += value
    return total


def to_camel_case(text: str):
    if type(text) != str:
        raise ValueError(f"Only strings allowed, not {type(text)}")

    words = re.split(r"[^a-zA-Z0-9]", text)  # Split on non-alphanumeric characters
    return "".join(
        word.capitalize() for word in words if word
    )  # Capitalize each word and join


def to_valid_method_name(s: str) -> str:
    """
    Convert a string to be a valid variable name:
    - Replace all characters that are not letters, numbers, or underscores with underscores.
    - Prefix with an underscore if the resulting string starts with a number.
    - Ensure the result is all lowercase.
    """
    if type(s) != str:
        raise ValueError(f"Only strings allowed, not {type(s)}")

    # Remove invalid characters and ensure lowercase
    s = re.sub(r"\W|^(?=\d)", "_", s).lower()

    # Ensure the string does not start with a number
    if re.match(r"^\d", s):
        s = "_" + s

    return s


def UK_to_ISO(date_str):
    return DateTimeHelper().UK_to_ISO(date_str)
