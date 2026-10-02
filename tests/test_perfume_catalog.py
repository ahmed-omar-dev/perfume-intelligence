import pytest

from models.perfume import Perfume
from models.perfume_catalog import PerfumeCatalog

from exceptions.custom_exceptions import (
    DuplicatePerfumeError,
    PerfumeNotFoundError,
)


# Creates a valid perfume object for testing.
def create_perfume(
    perfume_id="P001",
    stock_quantity=5,
):
    return Perfume(
        perfume_id=perfume_id,
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
        stock_quantity=stock_quantity,
    )


# Tests adding a perfume to the catalog.
def test_add_perfume():
    catalog = PerfumeCatalog()

    perfume = create_perfume()

    catalog.add_perfume(perfume)

    assert len(catalog) == 1


# Tests retrieving a perfume by ID.
def test_get_perfume():
    catalog = PerfumeCatalog()

    perfume = create_perfume()

    catalog.add_perfume(perfume)

    result = catalog.get_perfume("P001")

    assert result is perfume


# Tests removing a perfume.
def test_remove_perfume():
    catalog = PerfumeCatalog()

    perfume = create_perfume()

    catalog.add_perfume(perfume)

    removed_perfume = catalog.remove_perfume(
        "P001"
    )

    assert removed_perfume is perfume
    assert len(catalog) == 0


# Tests that duplicate perfume IDs are rejected.
def test_duplicate_perfume():
    catalog = PerfumeCatalog()

    perfume1 = create_perfume(
        perfume_id="P001"
    )

    perfume2 = create_perfume(
        perfume_id="P001"
    )

    catalog.add_perfume(perfume1)

    with pytest.raises(
        DuplicatePerfumeError
    ):
        catalog.add_perfume(
            perfume2
        )


# Tests getting a missing perfume.
def test_perfume_not_found():
    catalog = PerfumeCatalog()

    with pytest.raises(
        PerfumeNotFoundError
    ):
        catalog.get_perfume(
            "P999"
        )


# Tests getting all perfumes.
def test_all_perfumes():
    catalog = PerfumeCatalog()

    perfume1 = create_perfume(
        perfume_id="P001"
    )

    perfume2 = create_perfume(
        perfume_id="P002"
    )

    catalog.add_perfume(perfume1)
    catalog.add_perfume(perfume2)

    perfumes = catalog.all_perfumes()

    assert len(perfumes) == 2
    assert perfume1 in perfumes
    assert perfume2 in perfumes


# Tests low-stock filtering.
def test_low_stock_perfumes():
    catalog = PerfumeCatalog()

    perfume1 = create_perfume(
        perfume_id="P001",
        stock_quantity=2,
    )

    perfume2 = create_perfume(
        perfume_id="P002",
        stock_quantity=10,
    )

    catalog.add_perfume(perfume1)
    catalog.add_perfume(perfume2)

    results = (
        catalog.low_stock_perfumes()
    )

    assert len(results) == 1
    assert perfume1 in results
    assert perfume2 not in results


# Tests catalog length.
def test_catalog_length():
    catalog = PerfumeCatalog()

    assert len(catalog) == 0

    catalog.add_perfume(
        create_perfume()
    )

    assert len(catalog) == 1


# Tests ID membership in the catalog.
def test_catalog_contains():
    catalog = PerfumeCatalog()

    catalog.add_perfume(
        create_perfume(
            perfume_id="P001"
        )
    )

    assert "P001" in catalog
    assert "P999" not in catalog