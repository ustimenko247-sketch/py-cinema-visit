from typing import List, Dict


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    for customer in customers:
        food = customer["food"]
        name = customer["name"]
        print(f"{name} bought {food}")

    print(f"Movie '{movie}' started in hall {hall_number}")

    for customer in customers:
        print(f"{customer['name']} is watching '{movie}'")

    print(f"Movie '{movie}' ended in hall {hall_number}")
    print(f"{cleaner} is cleaning hall {hall_number}")
