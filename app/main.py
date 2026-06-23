from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    customer_objects = []

    for customer in customers:
        customer_obj = Customer(customer["name"])
        customer_objects.append(customer_obj)

        if customer.get("food"):
            CinemaBar.sell_product(customer_obj, customer["food"])

    hall.start_movie(movie)

    for customer_obj in customer_objects:
        customer_obj.watch_movie(movie)

    hall.end_movie(movie)

    cleaner_obj.clean_hall(hall_number)


if __name__ == "__main__":
    cinema_visit(
        customers=[
            {"name": "Denys", "food": "Coca-Cola"},
            {"name": "Ivan", "food": "Popcorn"},
        ],
        hall_number=1,
        cleaner="Petro",
        movie="Inception"
    )