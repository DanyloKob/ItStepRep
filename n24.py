class Product:
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price
    def info(self):
        return f"{self.name} - {self.price} грн"

class Customer:
    def __init__(self, name=None):
        self.name = name
        self.cart = []
    def add_to_cart(self, product):
        self.cart.append(product)
    def show_cart(self):
        print(f"Покупець: {self.name}")
        total = 0
        for product in self.cart:
            print(product.info())
            total += product.price
        print(f"Загальна вартість: {total}")

product1 = Product("Гіпер лате", 300)
product2 = Product("Тортик", 100)
product3 = Product("Чай", 45)
customer1 = Customer("Данило")
customer1.add_to_cart(product1)
customer1.add_to_cart(product2)
customer1.show_cart()

customer2 = Customer("Юля")
customer2.add_to_cart(product2)
customer2.add_to_cart(product3)
customer2.show_cart()