from app.cinema.bar import CinemaBar

class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self, movie, customers, cleaner):
        # початок фільму
        print(f'"{movie}" started in hall number {self.number}.')

        # перегляд фільму
        for customer in customers:
            customer.watch_movie(movie)

        # завершення фільму
        print(f'"{movie}" ended.')

        # прибирання залу
        cleaner.clean_hall(self.number)
