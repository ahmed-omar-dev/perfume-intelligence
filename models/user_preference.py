from utils.validators import (
    validate_positive_number,
    validate_string_list,
    validate_score,
)


class UserPreference:
    def __init__(
        self,
        max_budget,
        preferred_notes,
        preferred_seasons,
        preferred_occasions,
        minimum_longevity,
        minimum_sillage,
    ):
        self.max_budget = validate_positive_number(
            max_budget,
            "Max Budget",
        )

        self.preferred_notes = validate_string_list(
            preferred_notes,
            "Preferred Notes",
        )

        self.preferred_seasons = validate_string_list(
            preferred_seasons,
            "Preferred Seasons",
        )

        self.preferred_occasions = validate_string_list(
            preferred_occasions,
            "Preferred Occasions",
        )

        self.minimum_longevity = validate_score(
            minimum_longevity,
            "Minimum Longevity",
        )

        self.minimum_sillage = validate_score(
            minimum_sillage,
            "Minimum Sillage",
        )

    def to_dict(self):
        return {
            "max_budget": self.max_budget,
            "preferred_notes": self.preferred_notes,
            "preferred_seasons": self.preferred_seasons,
            "preferred_occasions": self.preferred_occasions,
            "minimum_longevity": self.minimum_longevity,
            "minimum_sillage": self.minimum_sillage,
        }