from __future__ import annotations
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    customer_objects: list[Customer] = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer.get("food"))
        customer_objects.append(customer_obj)

        if customer.get("food"):
            CinemaBar.sell_product(customer_obj, customer["food"])

    hall.movie_session(movie, customer_objects, cleaner_obj)
