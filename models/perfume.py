from utils.validators import (
    validate_non_empty_string,
    validate_price,
    validate_stock,
    validate_rating,
    validate_score,
    validate_positive_number,
    validate_string_list,
)


class Perfume:
    def __init__(
        self,
        perfume_id: str,
        name: str,
        brand: str,
        fragrance_family: str,
        top_notes: list,
        middle_notes: list,
        base_notes: list,
        price: float,
        size_ml: float,
        longevity: float,
        sillage: float,
        seasons: list,
        occasions: list,
        rating: float,
        stock_quantity: int,
    ):
        self.perfume_id = validate_non_empty_string(
            perfume_id,
            "Perfume ID",
        )

        self.name = validate_non_empty_string(
            name,
            "Name",
        )

        self.brand = validate_non_empty_string(
            brand,
            "Brand",
        )

        self.fragrance_family = validate_non_empty_string(
            fragrance_family,
            "Fragrance Family",
        )

        self.top_notes = validate_string_list(
            top_notes,
            "Top Notes",
        )

        self.middle_notes = validate_string_list(
            middle_notes,
            "Middle Notes",
        )

        self.base_notes = validate_string_list(
            base_notes,
            "Base Notes",
        )

        self.price = validate_price(
            price
        )

        self.size_ml = validate_positive_number(
            size_ml,
            "Size",
        )

        self.longevity = validate_score(
            longevity,
            "Longevity",
        )

        self.sillage = validate_score(
            sillage,
            "Sillage",
        )

        self.seasons = validate_string_list(
            seasons,
            "Seasons",
        )

        self.occasions = validate_string_list(
            occasions,
            "Occasions",
        )

        self.rating = validate_rating(
            rating
        )

        self.stock_quantity = validate_stock(
            stock_quantity
        )

    def is_low_stock(self):
        return self.stock_quantity <= 3

    def to_dict(self):
        return {
            "perfume_id": self.perfume_id,
            "name": self.name,
            "brand": self.brand,
            "fragrance_family": self.fragrance_family,
            "top_notes": self.top_notes,
            "middle_notes": self.middle_notes,
            "base_notes": self.base_notes,
            "price": self.price,
            "size_ml": self.size_ml,
            "longevity": self.longevity,
            "sillage": self.sillage,
            "seasons": self.seasons,
            "occasions": self.occasions,
            "rating": self.rating,
            "stock_quantity": self.stock_quantity,
        }
        