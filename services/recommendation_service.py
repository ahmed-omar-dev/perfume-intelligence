from models.perfume import Perfume
from models.user_preference import UserPreference


class RecommendationService:
    def calculate_score(self, perfume, preference):
        score = 0

        if perfume.price <= preference.max_budget:
            score += 2

        if perfume.longevity >= preference.minimum_longevity:
            score += 1

        if perfume.sillage >= preference.minimum_sillage:
            score += 1

        all_notes = (
            perfume.top_notes
            + perfume.middle_notes
            + perfume.base_notes
        )

        all_notes = [
            note.lower()
            for note in all_notes
        ]

        if any(
            preferred_note.lower() in all_notes
            for preferred_note in preference.preferred_notes
        ):
            score += 3

        perfume_seasons = [
            season.lower()
            for season in perfume.seasons
        ]

        if any(
            preferred_season.lower() in perfume_seasons
            for preferred_season in preference.preferred_seasons
        ):
            score += 2

        perfume_occasions = [
            occasion.lower()
            for occasion in perfume.occasions
        ]

        if any(
            preferred_occasion.lower() in perfume_occasions
            for preferred_occasion in preference.preferred_occasions
        ):
            score += 2

        return score


    def recommend(self, perfumes, preference):
        scored_perfumes = []

        for perfume in perfumes:
            score = self.calculate_score(
                perfume,
                preference,
            )

            scored_perfumes.append(
                (perfume, score)
            )

        scored_perfumes.sort(
            key=lambda item: item[1],
            reverse=True,
        )

        return scored_perfumes
    