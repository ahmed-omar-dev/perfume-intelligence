from models.perfume import Perfume

from exceptions.custom_exceptions import (
    DuplicatePerfumeError,
    PerfumeNotFoundError,
)


class PerfumeCatalog:
    def __init__(self):
        self._perfumes = {}

    def add_perfume(self, perfume):
        if not isinstance(perfume, Perfume):
            raise TypeError(
                "Expected a Perfume object."
            )

        if perfume.perfume_id in self._perfumes:
            raise DuplicatePerfumeError(
                f"Perfume with ID '{perfume.perfume_id}' already exists."
            )

        self._perfumes[perfume.perfume_id] = perfume

    def get_perfume(self, perfume_id):
        if perfume_id not in self._perfumes:
            raise PerfumeNotFoundError(
                f"Perfume with ID '{perfume_id}' not found."
            )  

        return self._perfumes[perfume_id]

    def remove_perfume(self, perfume_id):
        perfume = self.get_perfume(
            perfume_id
        )

        del self._perfumes[perfume_id]

        return perfume

    def all_perfumes(self):
        return list(
            self._perfumes.values()
        )

    def low_stock_perfumes(self):
        return [
            perfume
            for perfume in self._perfumes.values()
            if perfume.is_low_stock()
        ]

    def __len__(self):
        return len(
            self._perfumes
        )

    def __contains__(self, perfume_id):
        return perfume_id in self._perfumes
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
        return self.catalog.get_perfume(
            perfume_id
        )


    def delete_perfume(self, perfume_id):
        perfume = self.catalog.remove_perfume(
            perfume_id
        )

        self.save_perfumes()

        return perfume


    def get_all_perfumes(self):
        return self.catalog.all_perfumes()


    def get_low_stock_perfumes(self):
        return self.catalog.low_stock_perfumes()
    