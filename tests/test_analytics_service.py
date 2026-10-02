from models.perfume import Perfume
from services.analytics_service import AnalyticsService


# Creates perfume objects for analytics tests.
def create_perfumes():
    perfume1 = Perfume(
        perfume_id="P001",
        name="Perfume One",
        brand="Dior",
        fragrance_family="Woody",
        top_notes=["Bergamot"],
        middle_notes=["Lavender"],
        base_notes=["Vanilla"],
        price=2000,
        size_ml=100,
        longevity=8,
        sillage=7,
        seasons=["Winter"],
        occasions=["Evening"],
        rating=4.0,
        stock_quantity=2,
    )

    perfume2 = Perfume(
        perfume_id="P002",
        name="Perfume Two",
        brand="Chanel",
        fragrance_family="Fresh",
        top_notes=["Lemon"],
        middle_notes=["Mint"],
        base_notes=["Musk"],
        price=4000,
        size_ml=100,
        longevity=7,
        sillage=6,
        seasons=["Summer"],
        occasions=["Daily"],
        rating=5.0,
        stock_quantity=10,
    )

    return [
        perfume1,
        perfume2,
    ]


# Tests average perfume price.
def test_average_price():
    perfumes = create_perfumes()

    analytics = AnalyticsService(
        perfumes
    )

    assert analytics.average_price() == 3000.0


# Tests average perfume rating.
def test_average_rating():
    perfumes = create_perfumes()

    analytics = AnalyticsService(
        perfumes
    )

    assert analytics.average_rating() == 4.5


# Tests highest rated perfume.
def test_highest_rated_perfume():
    perfumes = create_perfumes()

    analytics = AnalyticsService(
        perfumes
    )

    result = (
        analytics.highest_rated_perfume()
    )

    assert result.name == "Perfume Two"


# Tests lowest price perfume.
def test_lowest_price_perfume():
    perfumes = create_perfumes()

    analytics = AnalyticsService(
        perfumes
    )

    result = (
        analytics.lowest_price_perfume()
    )

    assert result.name == "Perfume One"


# Tests highest price perfume.
def test_highest_price_perfume():
    perfumes = create_perfumes()

    analytics = AnalyticsService(
        perfumes
    )

    result = (
        analytics.highest_price_perfume()
    )

    assert result.name == "Perfume Two"


# Tests perfume counting by brand.
def test_count_by_brand():
    perfumes = create_perfumes()

    analytics = AnalyticsService(
        perfumes
    )

    result = analytics.count_by_brand()

    assert result["Dior"] == 1
    assert result["Chanel"] == 1


# Tests perfume counting by family.
def test_count_by_family():
    perfumes = create_perfumes()

    analytics = AnalyticsService(
        perfumes
    )

    result = analytics.count_by_family()

    assert result["Woody"] == 1
    assert result["Fresh"] == 1


# Tests top perfumes sorting.
def test_top_n_perfumes():
    perfumes = create_perfumes()

    analytics = AnalyticsService(
        perfumes
    )

    result = analytics.top_n_perfumes(1)

    assert len(result) == 1
    assert result[0].name == "Perfume Two"


# Tests low stock counting.
def test_low_stock_count():
    perfumes = create_perfumes()

    analytics = AnalyticsService(
        perfumes
    )

    assert analytics.low_stock_count() == 1