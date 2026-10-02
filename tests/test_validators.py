import pytest

from utils.validators import (
    validate_non_empty_string,
    validate_price,
    validate_stock,
    validate_rating,
    validate_score,
    validate_positive_number,
    validate_string_list,
)

from exceptions.custom_exceptions import (
    InvalidPriceError,
    InvalidRatingError,
    InvalidStockError,
    InvalidScoreError,
)


# Tests a valid non-empty string.
def test_valid_non_empty_string():
    result = validate_non_empty_string(
        "  Dior  ",
        "Brand",
    )

    assert result == "Dior"


# Tests that whitespace-only strings are rejected.
def test_empty_string():
    with pytest.raises(ValueError):
        validate_non_empty_string(
            "   ",
            "Brand",
        )


# Tests that non-string values are rejected.
def test_non_string_value():
    with pytest.raises(TypeError):
        validate_non_empty_string(
            123,
            "Brand",
        )


# Tests a valid price.
def test_valid_price():
    result = validate_price(100)

    assert result == 100.0


# Tests that zero price is rejected.
def test_zero_price():
    with pytest.raises(InvalidPriceError):
        validate_price(0)


# Tests that negative price is rejected.
def test_negative_price():
    with pytest.raises(InvalidPriceError):
        validate_price(-50)


# Tests that string price is rejected.
def test_price_string():
    with pytest.raises(TypeError):
        validate_price("100")


# Tests that boolean price is rejected.
def test_price_boolean():
    with pytest.raises(TypeError):
        validate_price(True)


# Tests a valid stock value.
def test_valid_stock():
    result = validate_stock(10)

    assert result == 10


# Tests that zero stock is allowed.
def test_zero_stock():
    result = validate_stock(0)

    assert result == 0


# Tests that negative stock is rejected.
def test_negative_stock():
    with pytest.raises(InvalidStockError):
        validate_stock(-1)


# Tests that float stock is rejected.
def test_float_stock():
    with pytest.raises(TypeError):
        validate_stock(2.5)


# Tests that boolean stock is rejected.
def test_boolean_stock():
    with pytest.raises(TypeError):
        validate_stock(True)


# Tests a valid rating.
def test_valid_rating():
    result = validate_rating(4.5)

    assert result == 4.5


# Tests minimum valid rating.
def test_min_rating():
    result = validate_rating(0)

    assert result == 0.0


# Tests maximum valid rating.
def test_max_rating():
    result = validate_rating(5)

    assert result == 5.0


# Tests rating below allowed range.
def test_rating_below_range():
    with pytest.raises(InvalidRatingError):
        validate_rating(-1)


# Tests rating above allowed range.
def test_rating_above_range():
    with pytest.raises(InvalidRatingError):
        validate_rating(6)


# Tests non-numeric rating.
def test_rating_string():
    with pytest.raises(TypeError):
        validate_rating("5")


# Tests a valid score.
def test_valid_score():
    result = validate_score(
        8,
        "Longevity",
    )

    assert result == 8.0


# Tests minimum valid score.
def test_min_score():
    result = validate_score(
        1,
        "Longevity",
    )

    assert result == 1.0


# Tests maximum valid score.
def test_max_score():
    result = validate_score(
        10,
        "Sillage",
    )

    assert result == 10.0


# Tests score below range.
def test_score_below_range():
    with pytest.raises(InvalidScoreError):
        validate_score(
            0,
            "Longevity",
        )


# Tests score above range.
def test_score_above_range():
    with pytest.raises(InvalidScoreError):
        validate_score(
            11,
            "Sillage",
        )


# Tests a valid positive number.
def test_valid_positive_number():
    result = validate_positive_number(
        100,
        "Size",
    )

    assert result == 100.0


# Tests zero positive number.
def test_zero_positive_number():
    with pytest.raises(ValueError):
        validate_positive_number(
            0,
            "Size",
        )


# Tests negative positive number.
def test_negative_positive_number():
    with pytest.raises(ValueError):
        validate_positive_number(
            -20,
            "Size",
        )


# Tests a valid string list.
def test_valid_string_list():
    result = validate_string_list(
        [
            " Vanilla ",
            " Oud ",
        ],
        "Notes",
    )

    assert result == [
        "Vanilla",
        "Oud",
    ]


# Tests non-list input.
def test_non_list_value():
    with pytest.raises(TypeError):
        validate_string_list(
            "Vanilla",
            "Notes",
        )


# Tests non-string item inside the list.
def test_non_string_list_item():
    with pytest.raises(TypeError):
        validate_string_list(
            [
                "Vanilla",
                10,
            ],
            "Notes",
        )


# Tests empty string inside the list.
def test_empty_string_list_item():
    with pytest.raises(ValueError):
        validate_string_list(
            [
                "Vanilla",
                "   ",
            ],
            "Notes",
        )