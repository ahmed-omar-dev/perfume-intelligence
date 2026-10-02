from models.perfume import Perfume


class AnalyticsService:
    def __init__(self, perfumes):
        self.perfumes = perfumes

    def average_price(self):
        if not self.perfumes:
            return 0.0

        total_price = sum(
            perfume.price
            for perfume in self.perfumes
        )

        return total_price / len(self.perfumes)

    def average_rating(self):
        if not self.perfumes:
            return 0.0

        total_rating = sum(
            perfume.rating
            for perfume in self.perfumes
        )

        return total_rating / len(self.perfumes)

    def highest_rated_perfume(self):
        if not self.perfumes:
            return None

        return max(
            self.perfumes,
            key=lambda perfume: perfume.rating
        )

    def lowest_price_perfume(self):
        if not self.perfumes:
            return None

        return min(
            self.perfumes,
            key=lambda perfume: perfume.price
        )

    def highest_price_perfume(self):
        if not self.perfumes:
            return None

        return max(
            self.perfumes,
            key=lambda perfume: perfume.price
        )

    def count_by_brand(self):
        brand_counts = {}

        for perfume in self.perfumes:
            brand = perfume.brand

            brand_counts[brand] = (
                brand_counts.get(brand, 0) + 1
            )

        return brand_counts

    def count_by_family(self):
        family_counts = {}

        for perfume in self.perfumes:
            family = perfume.fragrance_family

            family_counts[family] = (
                family_counts.get(family, 0) + 1
            )

        return family_counts

    def top_n_perfumes(self, n=5):
        sorted_perfumes = sorted(
            self.perfumes,
            key=lambda perfume: perfume.rating,
            reverse=True
        )

        return sorted_perfumes[:n]

    def low_stock_count(self):
        return sum(
            1
            for perfume in self.perfumes
            if perfume.is_low_stock()
        )