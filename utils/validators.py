from exceptions.custom_exceptions import (
    InvalidPriceError,
    InvalidRatingError,
    InvalidStockError,
    InvalidScoreError,
)


def validate_non_empty_string(value, field_name):
    if not isinstance(value, str):
        raise TypeError(
            f"{field_name} must be a string."
        )

    clean_value = value.strip()

    if not clean_value:
        raise ValueError(
            f"{field_name} cannot be empty or contain only whitespace."
        )

    return clean_value


def validate_price(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(
            "Price must be an integer or float."
        )

    if value <= 0:
        raise InvalidPriceError(
            "Price must be greater than zero."
        )

    return float(value)


def validate_stock(value):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(
            "Stock must be an integer."
        )

    if value < 0:
        raise InvalidStockError(
            "Stock cannot be negative."
        )

    return value


def validate_rating(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(
            "Rating must be a number."
        )

    if not 0 <= value <= 5:
        raise InvalidRatingError(
            "Rating must be between 0 and 5."
        )

    return float(value)


def validate_score(value, field_name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(
            f"{field_name} must be a number."
        )

    if not 1 <= value <= 10:
        raise InvalidScoreError(
            f"{field_name} must be between 1 and 10."
        )

    return float(value)

def validate_positive_number(value, field_name):
    if isinstance (value, bool) or not isinstance (value, (int, float)):
        raise TypeError ("Pls positive number.")
    if value <= 0:
        raise ValueError("Pls must be number grater than zero.")
    return float(value)


def validate_positive_number(value, field_name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(
            f"{field_name} must be a number."
        )

    if value <= 0:
        raise ValueError(
            f"{field_name} must be greater than zero."
        )

    return float(value)

def validate_string_list(value, field_name):
    if not isinstance(value, list):
        raise TypeError(
            f"{field_name} must be a list."
        )

    clean_list = []

    for item in value:
        if not isinstance(item, str):
            raise TypeError(
                f"All items in {field_name} must be strings."
            )

        clean_item = item.strip()

        if not clean_item:
            raise ValueError(
                f"{field_name} cannot contain empty strings or whitespace."
            )

        clean_list.append(clean_item)

    return clean_list

