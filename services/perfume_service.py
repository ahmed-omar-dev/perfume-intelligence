from models.perfume import Perfume


class PerfumeService:
    def __init__(
        self,
        catalog,
        storage,
    ):
        self.catalog = catalog
        self.storage = storage

    def load_perfumes(self):
        data = self.storage.load()

        for item in data:
            perfume = Perfume(
                perfume_id=item["perfume_id"],
                name=item["name"],
                brand=item["brand"],
                fragrance_family=item["fragrance_family"],
                top_notes=item["top_notes"],
                middle_notes=item["middle_notes"],
                base_notes=item["base_notes"],
                price=item["price"],
                size_ml=item["size_ml"],
                longevity=item["longevity"],
                sillage=item["sillage"],
                seasons=item["seasons"],
                occasions=item["occasions"],
                rating=item["rating"],
                stock_quantity=item["stock_quantity"],
            )

            self.catalog.add_perfume(perfume)

    def save_perfumes(self):
        data = [
            perfume.to_dict()
            for perfume in self.catalog.all_perfumes()
        ]

        self.storage.save(data)

    def create_perfume(
        self,
        perfume_id,
        name,
        brand,
        fragrance_family,
        top_notes,
        middle_notes,
        base_notes,
        price,
        size_ml,
        longevity,
        sillage,
        seasons,
        occasions,
        rating,
        stock_quantity,
    ):
        perfume = Perfume(
            perfume_id=perfume_id,
            name=name,
            brand=brand,
            fragrance_family=fragrance_family,
            top_notes=top_notes,
            middle_notes=middle_notes,
            base_notes=base_notes,
            price=price,
            size_ml=size_ml,
            longevity=longevity,
            sillage=sillage,
            seasons=seasons,
            occasions=occasions,
            rating=rating,
            stock_quantity=stock_quantity,
        )

        self.catalog.add_perfume(perfume)
        self.save_perfumes()

        return perfume

    def get_perfume(self, perfume_id):
        return self.catalog.get_perfume(perfume_id)

    def delete_perfume(self, perfume_id):
        perfume = self.catalog.remove_perfume(perfume_id)

        self.save_perfumes()

        return perfume

    def get_all_perfumes(self):
        return self.catalog.all_perfumes()

    def get_low_stock_perfumes(self):
        return self.catalog.low_stock_perfumes()