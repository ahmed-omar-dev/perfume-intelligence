import pytest

from models.perfume import Perfume

from exceptions.custom_exceptions import (
    InvalidPriceError,
    InvalidRatingError,
    InvalidStockError,
    InvalidScoreError,
)


# Creates a valid perfume object for testing.
def create_valid_perfume():
    return Perfume(
        perfume_id="P001",
        name="Test Perfume",
        brand="Test Brand",
        fragrance_family="Woody",
        top_notes=["Bergamot"],
        middle_notes=["Lavender"],
        base_notes=["Vanilla"],
        price=2500,
        size_ml=100,
        longevity=8,
        sillage=7,
        seasons=["Winter", "Fall"],
        occasions=["Evening"],
        rating=4.5,
        stock_quantity=5,
    )


# Tests that a valid perfume is created correctly.
def test_create_valid_perfume():
    perfume = create_valid_perfume()

    assert perfume.perfume_id == "P001"
    assert perfume.name == "Test Perfume"
    assert perfume.brand == "Test Brand"
    assert perfume.price == 2500.0
    assert perfume.rating == 4.5
    assert perfume.stock_quantity == 5


# Tests that invalid price is rejected.
def test_perfume_invalid_price():
    with pytest.raises(InvalidPriceError):
        Perfume(
            perfume_id="P001",
            name="Test Perfume",
            brand="Test Brand",
            fragrance_family="Woody",
            top_notes=["Bergamot"],
            middle_notes=["Lavender"],
            base_notes=["Vanilla"],
            price=-100,
            size_ml=100,
            longevity=8,
            sillage=7,
            seasons=["Winter"],
            occasions=["Evening"],
            rating=4.5,
            stock_quantity=5,
        )


# Tests that invalid rating is rejected.
def test_perfume_invalid_rating():
    with pytest.raises(InvalidRatingError):
        Perfume(
            perfume_id="P001",
            name="Test Perfume",
            brand="Test Brand",
            fragrance_family="Woody",
            top_notes=["Bergamot"],
            middle_notes=["Lavender"],
            base_notes=["Vanilla"],
            price=2500,
            size_ml=100,
            longevity=8,
            sillage=7,
            seasons=["Winter"],
            occasions=["Evening"],
            rating=6,
            stock_quantity=5,
        )


# Tests that invalid stock is rejected.
def test_perfume_invalid_stock():
    with pytest.raises(InvalidStockError):
        Perfume(
            perfume_id="P001",
            name="Test Perfume",
            brand="Test Brand",
            fragrance_family="Woody",
            top_notes=["Bergamot"],
            middle_notes=["Lavender"],
            base_notes=["Vanilla"],
            price=2500,
            size_ml=100,
            longevity=8,
            sillage=7,
            seasons=["Winter"],
            occasions=["Evening"],
            rating=4.5,
            stock_quantity=-1,
        )


# Tests that invalid longevity is rejected.
def test_perfume_invalid_longevity():
    with pytest.raises(InvalidScoreError):
        Perfume(
            perfume_id="P001",
            name="Test Perfume",
            brand="Test Brand",
            fragrance_family="Woody",
            top_notes=["Bergamot"],
            middle_notes=["Lavender"],
            base_notes=["Vanilla"],
            price=2500,
            size_ml=100,
            longevity=11,
            sillage=7,
            seasons=["Winter"],
            occasions=["Evening"],
            rating=4.5,
            stock_quantity=5,
        )


# Tests the low-stock business rule.
def test_is_low_stock():
    perfume = create_valid_perfume()

    perfume.stock_quantity = 3

    assert perfume.is_low_stock() is True


# Tests that normal stock is not considered low stock.
def test_is_not_low_stock():
    perfume = create_valid_perfume()

    perfume.stock_quantity = 10

    assert perfume.is_low_stock() is False


# Tests converting perfume object to dictionary.
def test_to_dict():
    perfume = create_valid_perfume()

    data = perfume.to_dict()

    assert data["perfume_id"] == "P001"
    assert data["name"] == "Test Perfume"
    assert data["brand"] == "Test Brand"
    assert data["price"] == 2500.0
    assert data["rating"] == 4.5