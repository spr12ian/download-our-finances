import locale
import math
import re


def all_conditions_are_false(conditions) -> bool:
    if not all_items_are_boolean(conditions):
        raise ValueError("Not all conditions are boolean")

    return not any(conditions)


def all_items_are_boolean(lst) -> bool:
    return all(isinstance(item, bool) for item in lst)


def crop(string, excess) -> str:
    excess_length = len(excess)
    if string[-excess_length:] == excess:
        string = string[:-excess_length]
    return string


def format_as_gbp(amount: float, field_width: int = 10) -> str:
    """
    Format a float as GBP.
    """
    # Set the locale to GBP
    locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")

    # Format the float as currency
    formatted_amount = locale.currency(amount, grouping=True)

    # Right justify the formatted amount within the specified field width
    return f"{formatted_amount:>{field_width}}"


def format_as_gbp_or_blank(amount) -> str:
    """
    Format a float as GBP or blank if zero.
    """

    if abs(amount) < 0.01:
        return ""
    else:
        # Format the float as currency
        return format_as_gbp(amount)


def round_down(number: float) -> int:
    return math.floor(number)


def round_up(number: float) -> int:
    return math.ceil(number)


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


def to_valid_method_name(s) -> str:
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
    # Prefix with an underscore if the first character is a digit
    if s and s[0].isdigit():
        s = "_" + s
    return s
