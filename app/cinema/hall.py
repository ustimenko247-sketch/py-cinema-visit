class CinemaHall:
    def __init__(self, hall_number: int):
        self.hall_number = hall_number
        self.is_open = False

    def open(self):
        self.is_open = True
        print(f"Hall {self.hall_number} is open")

    def start_movie(self, movie: str):
        print(f"Movie '{movie}' started in hall {self.hall_number}")

    def end_movie(self, movie: str):
        print(f"Movie '{movie}' ended in hall {self.hall_number}")