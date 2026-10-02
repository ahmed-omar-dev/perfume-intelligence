from models.perfume import Perfume
from services.search_service import SearchService


# Creates perfume objects for search tests.
def create_perfumes():
    perfume1 = Perfume(
        perfume_id="P001",
        name="Sauvage",
        brand="Dior",
        fragrance_family="Aromatic",
        top_notes=["Bergamot"],
        middle_notes=["Lavender"],
        base_notes=["Ambroxan"],
        price=3000,
        size_ml=100,
        longevity=8,
        sillage=8,
        seasons=["Summer", "Spring"],
        occasions=["Daily", "Office"],
        rating=4.5,
        stock_quantity=5,
    )

    perfume2 = Perfume(
        perfume_id="P002",
        name="Oud Wood",
        brand="Tom Ford",
        fragrance_family="Woody",
        top_notes=["Rosewood"],
        middle_notes=["Sandalwood"],
        base_notes=["Oud"],
        price=5000,
        size_ml=100,
        longevity=9,
        sillage=7,
        seasons=["Winter", "Fall"],
        occasions=["Evening"],
        rating=4.8,
        stock_quantity=4,
    )

    return [
        perfume1,
        perfume2,
    ]


# Tests searching perfumes by name.
def test_search_by_name():
    perfumes = create_perfumes()

    search_service = SearchService(
        perfumes
    )

    results = (
        search_service.search_by_name(
            "sauv"
        )
    )

    assert len(results) == 1
    assert results[0].name == "Sauvage"


# Tests searching perfumes by brand.
def test_search_by_brand():
    perfumes = create_perfumes()

    search_service = SearchService(
        perfumes
    )

    results = (
        search_service.search_by_brand(
            "dior"
        )
    )

    assert len(results) == 1
    assert results[0].brand == "Dior"


# Tests filtering perfumes by family.
def test_filter_by_family():
    perfumes = create_perfumes()

    search_service = SearchService(
        perfumes
    )

    results = (
        search_service.filter_by_family(
            "woody"
        )
    )

    assert len(results) == 1
    assert results[0].name == "Oud Wood"


# Tests filtering perfumes by season.
def test_filter_by_season():
    perfumes = create_perfumes()

    search_service = SearchService(
        perfumes
    )

    results = (
        search_service.filter_by_season(
            "winter"
        )
    )

    assert len(results) == 1
    assert results[0].name == "Oud Wood"


# Tests filtering perfumes by note.
def test_filter_by_note():
    perfumes = create_perfumes()

    search_service = SearchService(
        perfumes
    )

    results = (
        search_service.filter_by_note(
            "oud"
        )
    )

    assert len(results) == 1
    assert results[0].name == "Oud Wood"


# Tests filtering perfumes by maximum price.
def test_filter_by_max_price():
    perfumes = create_perfumes()

    search_service = SearchService(
        perfumes
    )

    results = (
        search_service.filter_by_max_price(
            3500
        )
    )

    assert len(results) == 1
    assert results[0].name == "Sauvage"


# Tests sorting perfumes by price.
def test_sort_by_price():
    perfumes = create_perfumes()

    search_service = SearchService(
        perfumes
    )

    results = (
        search_service.sort_by_price()
    )

    assert results[0].price == 3000.0
    assert results[1].price == 5000.0


# Tests sorting perfumes by rating.
def test_sort_by_rating():
    perfumes = create_perfumes()

    search_service = SearchService(
        perfumes
    )

    results = (
        search_service.sort_by_rating()
    )

    assert results[0].rating == 4.8
    assert results[1].rating == 4.5