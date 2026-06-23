def cinema_visit(customers, hall_number, cleaner, movie) -> None:
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    customer_objects = []

    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        customer_objects.append(customer_obj)

        CinemaBar.sell_product(customer["food"], customer_obj)

    hall.movie_session(movie, customer_objects, cleaner_obj)
