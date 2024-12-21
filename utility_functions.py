import re


# Function to convert currency/percent strings to float
def string_to_float(string):
    if string.strip() == "":  # Check if the string is empty or whitespace
        return 0.0

    # Remove the currency symbol (£), commas, and percent then convert to float
    return float(re.sub(r"[£,%]", "", string))


def to_valid_method_name(s):
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
