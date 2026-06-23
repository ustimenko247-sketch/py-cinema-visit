class CinemaBar:
    def __init__(self):
        self.menu = ["Coca-Cola", "Popcorn", "Beer"]

    def show_menu(self):
        print(self.menu)

    def order(self, product: str):
        if product in self.menu:
            return f"You ordered {product}"
        return "Product not available"

    @staticmethod
    def sell_product(customer, product: str):
        print(f"{customer.name} bought {product}")