from app.cinema_visit import cinema_visit

if __name__ == "__main__":
    customers = [
        {"name": "Alex", "food": "popcorn"},
        {"name": "Іван", "food": "чіпси"}
    ]
    cinema_visit(
        customers,
        hall_number=1,
        cleaner="Петро",
        movie="Inception"
    )
