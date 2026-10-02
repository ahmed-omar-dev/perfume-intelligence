from models.perfume_catalog import PerfumeCatalog
from models.user_preference import UserPreference

from services.perfume_service import PerfumeService
from services.search_service import SearchService
from services.recommendation_service import RecommendationService
from services.analytics_service import AnalyticsService

from storage.json_storage import JSONStorage

from exceptions.custom_exceptions import PerfumeAppError


# Displays the main CLI menu.
def show_menu():
    print("\n=== Perfume Intelligence Platform ===")
    print("1. Add Perfume")
    print("2. View All Perfumes")
    print("3. Search Perfume")
    print("4. Filter Perfumes")
    print("5. Delete Perfume")
    print("6. Show Low Stock")
    print("7. Show Recommendations")
    print("8. Show Analytics")
    print("9. Exit")


# Reads a valid float number from the user.
def get_float_input(prompt):
    while True:
        try:
            return float(
                input(prompt).strip()
            )

        except ValueError:
            print(
                "Invalid input. Please enter a valid number."
            )


# Reads a valid integer from the user.
def get_int_input(prompt):
    while True:
        try:
            return int(
                input(prompt).strip()
            )

        except ValueError:
            print(
                "Invalid input. Please enter a valid integer."
            )


# Reads a comma-separated list from the user.
def get_list_input(prompt):
    return [
        item.strip()
        for item in input(prompt).split(",")
        if item.strip()
    ]


# Displays perfume objects in a readable format.
def display_perfumes(perfumes):
    if not perfumes:
        print("No perfumes found.")
        return

    for perfume in perfumes:
        print("\n------------------------------")
        print(f"ID: {perfume.perfume_id}")
        print(f"Name: {perfume.name}")
        print(f"Brand: {perfume.brand}")
        print(
            f"Family: "
            f"{perfume.fragrance_family}"
        )
        print(
            f"Top Notes: "
            f"{', '.join(perfume.top_notes)}"
        )
        print(
            f"Middle Notes: "
            f"{', '.join(perfume.middle_notes)}"
        )
        print(
            f"Base Notes: "
            f"{', '.join(perfume.base_notes)}"
        )
        print(f"Price: {perfume.price}")
        print(f"Size: {perfume.size_ml} ml")
        print(f"Longevity: {perfume.longevity}")
        print(f"Sillage: {perfume.sillage}")
        print(
            f"Seasons: "
            f"{', '.join(perfume.seasons)}"
        )
        print(
            f"Occasions: "
            f"{', '.join(perfume.occasions)}"
        )
        print(f"Rating: {perfume.rating}")
        print(
            f"Stock: "
            f"{perfume.stock_quantity}"
        )


# Collects perfume data and creates a new perfume.
def add_perfume_cli(service):
    try:
        perfume_id = input(
            "Perfume ID: "
        ).strip()

        name = input(
            "Name: "
        ).strip()

        brand = input(
            "Brand: "
        ).strip()

        fragrance_family = input(
            "Fragrance Family: "
        ).strip()

        top_notes = get_list_input(
            "Top Notes (comma-separated): "
        )

        middle_notes = get_list_input(
            "Middle Notes (comma-separated): "
        )

        base_notes = get_list_input(
            "Base Notes (comma-separated): "
        )

        price = get_float_input(
            "Price: "
        )

        size_ml = get_float_input(
            "Size in ml: "
        )

        longevity = get_float_input(
            "Longevity (1-10): "
        )

        sillage = get_float_input(
            "Sillage (1-10): "
        )

        seasons = get_list_input(
            "Seasons (comma-separated): "
        )

        occasions = get_list_input(
            "Occasions (comma-separated): "
        )

        rating = get_float_input(
            "Rating (0-5): "
        )

        stock_quantity = get_int_input(
            "Stock Quantity: "
        )

        perfume = service.create_perfume(
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

        print(
            f"Perfume '{perfume.name}' "
            f"added successfully."
        )

    except (
        PerfumeAppError,
        TypeError,
        ValueError,
    ) as error:
        print(
            f"Error: {error}"
        )


# Displays all perfumes in the catalog.
def view_all_perfumes_cli(service):
    perfumes = service.get_all_perfumes()

    display_perfumes(perfumes)


# Searches perfumes by name or brand.
def search_perfumes_cli(service):
    perfumes = service.get_all_perfumes()

    search_service = SearchService(
        perfumes
    )

    print("\n=== Search Perfume ===")
    print("1. Search by Name")
    print("2. Search by Brand")

    choice = input(
        "Choose search type: "
    ).strip()

    if choice == "1":
        query = input(
            "Enter perfume name: "
        ).strip()

        results = (
            search_service.search_by_name(
                query
            )
        )

        display_perfumes(results)

    elif choice == "2":
        brand = input(
            "Enter brand: "
        ).strip()

        results = (
            search_service.search_by_brand(
                brand
            )
        )

        display_perfumes(results)

    else:
        print(
            "Invalid search option."
        )


# Filters or sorts perfumes using selected criteria.
def filter_perfumes_cli(service):
    perfumes = service.get_all_perfumes()

    search_service = SearchService(
        perfumes
    )

    print("\n=== Filter Perfumes ===")
    print("1. Filter by Family")
    print("2. Filter by Season")
    print("3. Filter by Occasion")
    print("4. Filter by Note")
    print("5. Filter by Max Price")
    print("6. Sort by Price")
    print("7. Sort by Rating")

    choice = input(
        "Choose filter type: "
    ).strip()

    if choice == "1":
        family = input(
            "Enter fragrance family: "
        ).strip()

        results = (
            search_service.filter_by_family(
                family
            )
        )

    elif choice == "2":
        season = input(
            "Enter season: "
        ).strip()

        results = (
            search_service.filter_by_season(
                season
            )
        )

    elif choice == "3":
        occasion = input(
            "Enter occasion: "
        ).strip()

        results = (
            search_service.filter_by_occasion(
                occasion
            )
        )

    elif choice == "4":
        note = input(
            "Enter perfume note: "
        ).strip()

        results = (
            search_service.filter_by_note(
                note
            )
        )

    elif choice == "5":
        max_price = get_float_input(
            "Enter maximum price: "
        )

        results = (
            search_service.filter_by_max_price(
                max_price
            )
        )

    elif choice == "6":
        print("\n1. Lowest to Highest")
        print("2. Highest to Lowest")

        order = input(
            "Choose order: "
        ).strip()

        reverse = order == "2"

        results = (
            search_service.sort_by_price(
                reverse=reverse
            )
        )

    elif choice == "7":
        print("\n1. Highest to Lowest")
        print("2. Lowest to Highest")

        order = input(
            "Choose order: "
        ).strip()

        reverse = order != "2"

        results = (
            search_service.sort_by_rating(
                reverse=reverse
            )
        )

    else:
        print(
            "Invalid filter option."
        )
        return

    display_perfumes(results)


# Deletes a perfume using its ID.
def delete_perfume_cli(service):
    try:
        perfume_id = input(
            "Enter Perfume ID to delete: "
        ).strip()

        perfume = service.delete_perfume(
            perfume_id
        )

        print(
            f"Perfume '{perfume.name}' "
            f"deleted successfully."
        )

    except PerfumeAppError as error:
        print(
            f"Error: {error}"
        )


# Displays perfumes with low stock.
def show_low_stock_cli(service):
    perfumes = (
        service.get_low_stock_perfumes()
    )

    print("\n=== Low Stock Perfumes ===")

    display_perfumes(perfumes)


# Collects user preferences and shows recommendations.
def show_recommendations_cli(service):
    perfumes = service.get_all_perfumes()

    if not perfumes:
        print(
            "No perfumes available "
            "for recommendations."
        )
        return

    print(
        "\n=== Perfume Recommendations ==="
    )

    try:
        max_budget = get_float_input(
            "Maximum Budget: "
        )

        preferred_notes = get_list_input(
            "Preferred Notes "
            "(comma-separated): "
        )

        preferred_seasons = get_list_input(
            "Preferred Seasons "
            "(comma-separated): "
        )

        preferred_occasions = get_list_input(
            "Preferred Occasions "
            "(comma-separated): "
        )

        minimum_longevity = get_float_input(
            "Minimum Longevity (1-10): "
        )

        minimum_sillage = get_float_input(
            "Minimum Sillage (1-10): "
        )

        preference = UserPreference(
            max_budget=max_budget,
            preferred_notes=preferred_notes,
            preferred_seasons=preferred_seasons,
            preferred_occasions=preferred_occasions,
            minimum_longevity=minimum_longevity,
            minimum_sillage=minimum_sillage,
        )

        recommendation_service = (
            RecommendationService()
        )

        recommendations = (
            recommendation_service.recommend(
                perfumes,
                preference,
            )
        )

        if not recommendations:
            print(
                "No recommendations found."
            )
            return

        print(
            "\n=== Recommended Perfumes ==="
        )

        for perfume, score in recommendations:
            print(
                "\n------------------------------"
            )
            print(
                f"Name: {perfume.name}"
            )
            print(
                f"Brand: {perfume.brand}"
            )
            print(
                f"Price: {perfume.price}"
            )
            print(
                f"Rating: {perfume.rating}"
            )
            print(
                f"Recommendation Score: {score}"
            )

    except (
        PerfumeAppError,
        TypeError,
        ValueError,
    ) as error:
        print(
            f"Error: {error}"
        )


# Displays analytics about the perfume catalog.
def show_analytics_cli(service):
    perfumes = service.get_all_perfumes()

    if not perfumes:
        print(
            "No perfumes available "
            "for analytics."
        )
        return

    analytics = AnalyticsService(
        perfumes
    )

    print("\n=== Perfume Analytics ===")

    print(
        f"Total Perfumes: "
        f"{len(perfumes)}"
    )

    print(
        f"Average Price: "
        f"{analytics.average_price():.2f}"
    )

    print(
        f"Average Rating: "
        f"{analytics.average_rating():.2f}"
    )

    highest_rated = (
        analytics.highest_rated_perfume()
    )

    lowest_price = (
        analytics.lowest_price_perfume()
    )

    highest_price = (
        analytics.highest_price_perfume()
    )

    print(
        f"Highest Rated Perfume: "
        f"{highest_rated.name}"
    )

    print(
        f"Lowest Price Perfume: "
        f"{lowest_price.name}"
    )

    print(
        f"Highest Price Perfume: "
        f"{highest_price.name}"
    )

    print(
        f"Low Stock Count: "
        f"{analytics.low_stock_count()}"
    )

    print(
        "\nPerfumes by Brand:"
    )

    brand_counts = (
        analytics.count_by_brand()
    )

    for brand, count in brand_counts.items():
        print(
            f"{brand}: {count}"
        )

    print(
        "\nPerfumes by Family:"
    )

    family_counts = (
        analytics.count_by_family()
    )

    for family, count in family_counts.items():
        print(
            f"{family}: {count}"
        )

    print(
        "\nTop 5 Perfumes:"
    )

    top_perfumes = (
        analytics.top_n_perfumes(5)
    )

    for perfume in top_perfumes:
        print(
            f"{perfume.name} "
            f"- Rating: {perfume.rating}"
        )


# Starts and controls the application.
def main():
    catalog = PerfumeCatalog()

    storage = JSONStorage(
        "data/perfumes.json"
    )

    service = PerfumeService(
        catalog,
        storage,
    )

    try:
        service.load_perfumes()

    except (
        PerfumeAppError,
        TypeError,
        ValueError,
    ) as error:
        print(
            f"Could not load perfumes: {error}"
        )

    while True:
        show_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":
            add_perfume_cli(service)

        elif choice == "2":
            view_all_perfumes_cli(service)

        elif choice == "3":
            search_perfumes_cli(service)

        elif choice == "4":
            filter_perfumes_cli(service)

        elif choice == "5":
            delete_perfume_cli(service)

        elif choice == "6":
            show_low_stock_cli(service)

        elif choice == "7":
            show_recommendations_cli(
                service
            )

        elif choice == "8":
            show_analytics_cli(
                service
            )

        elif choice == "9":
            print(
                "Goodbye!"
            )
            break

        else:
            print(
                "Invalid option. "
                "Please try again."
            )


# Runs the program only when executed directly.
if __name__ == "__main__":
    main()