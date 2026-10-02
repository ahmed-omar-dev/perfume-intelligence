from models.perfume import Perfume
from models.user_preference import UserPreference
from services.recommendation_service import RecommendationService


# Creates a perfume for recommendation tests.
def create_perfume():
    return Perfume(
        perfume_id="P001",
        name="Oud Night",
        brand="Test Brand",
        fragrance_family="Woody",
        top_notes=["Bergamot"],
        middle_notes=["Rose"],
        base_notes=["Oud", "Vanilla"],
        price=2500,
        size_ml=100,
        longevity=9,
        sillage=8,
        seasons=["Winter"],
        occasions=["Evening"],
        rating=4.7,
        stock_quantity=5,
    )


# Creates user preferences for recommendation tests.
def create_preference():
    return UserPreference(
        max_budget=3000,
        preferred_notes=[
            "Oud",
            "Vanilla",
        ],
        preferred_seasons=[
            "Winter",
        ],
        preferred_occasions=[
            "Evening",
        ],
        minimum_longevity=8,
        minimum_sillage=7,
    )


# Tests calculating a full recommendation score.
def test_calculate_score():
    perfume = create_perfume()
    preference = create_preference()

    service = RecommendationService()

    score = service.calculate_score(
        perfume,
        preference,
    )

    assert score == 11


# Tests recommendation ordering.
def test_recommend_order():
    perfume1 = create_perfume()

    perfume2 = Perfume(
        perfume_id="P002",
        name="Fresh Day",
        brand="Test Brand",
        fragrance_family="Fresh",
        top_notes=["Lemon"],
        middle_notes=["Mint"],
        base_notes=["Musk"],
        price=4000,
        size_ml=100,
        longevity=5,
        sillage=5,
        seasons=["Summer"],
        occasions=["Daily"],
        rating=4.0,
        stock_quantity=5,
    )

    preference = create_preference()

    service = RecommendationService()

    results = service.recommend(
        [
            perfume1,
            perfume2,
        ],
        preference,
    )

    assert results[0][0] is perfume1
    assert results[0][1] > results[1][1]