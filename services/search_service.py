from models.perfume import Perfume

class SearchService:
    def __init__(self, perfumes_list):
        self.perfumes = perfumes_list


    def search_by_name(self, query):
        query = query.lower()

        return [
            perfume
            for perfume in self.perfumes
            if query in perfume.name.lower()
        ]


    def search_by_brand(self, brand):
        brand = brand.lower()

        return [
            perfume
            for perfume in self.perfumes
            if perfume.brand.lower() == brand
        ]


    def filter_by_family(self, family):
        family = family.lower()

        return [
            perfume
            for perfume in self.perfumes
            if perfume.fragrance_family.lower() == family
        ]


    def filter_by_season(self, season):
        season = season.lower()

        return [
            perfume
            for perfume in self.perfumes
            if season in [
                item.lower()
                for item in perfume.seasons
            ]
        ]


    def filter_by_occasion(self, occasion):
        occasion = occasion.lower()

        return [
            perfume
            for perfume in self.perfumes
            if occasion in [
                item.lower()
                for item in perfume.occasions
            ]
        ]


    def filter_by_note(self, note):
        note = note.lower()

        return [
            perfume
            for perfume in self.perfumes
            if (
                note in [
                    item.lower()
                    for item in perfume.top_notes
                ]
                or note in [
                    item.lower()
                    for item in perfume.middle_notes
                ]
                or note in [
                    item.lower()
                    for item in perfume.base_notes
                ]
            )
        ]


    def filter_by_max_price(self, max_price):
        return [
            perfume
            for perfume in self.perfumes
            if perfume.price <= max_price
        ]


    def sort_by_price(self, reverse=False):
        return sorted(
            self.perfumes,
            key=lambda perfume: perfume.price,
            reverse=reverse,
        )


    def sort_by_rating(self, reverse=True):
        return sorted(
            self.perfumes,
            key=lambda perfume: perfume.rating,
            reverse=reverse,
        )