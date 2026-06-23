from typing import List
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        customers: List[Customer],
        cleaning_staff: Cleaner,
    ) -> None:
        print(f"Movie session in hall number {self.number} started.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"Movie session in hall number {self.number} ended.")
        cleaning_staff.clean_hall(self.number)
