from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_info(self):
        pass

    def apply_discount(self, percent):
        p = 1 - percent / 100
        self.price = self.price * p
        print(f"Ціну змінено на {percent}%. Нова ціна {self.price} до продукту {self.name}")

class FoodProduct(Product):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self.expiration_date = expiration_date

    def get_info(self):
        print(f"Товар: {self.name}, Ціна: {self.price} грн, Термін придатності до: {self.expiration_date}")

    def new_expiration_date(self, newED):
        self.expiration_date = newED


class Tehnic(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

    def get_info(self):
        print(f"Товар: {self.name}, Ціна: {self.price} грн, Гарантія: {self.warranty_years} роки")

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, obj: Product):
        self.products.append(obj)

    def remove_product(self, name):
        self.products.remove(name)

    def show_card(self):
        if len(self.products) == 0:
            print(f"Ви ще нічого не замовили скотиняка безсовісна!")
            return
        for p in self.products:
            print(p.name)

    def apply_discount_to_all(self, percent):
        for product in self.products:
            product.apply_discount(percent)

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def find_product_by_name(self, keyword):
        for i in range(len(self.products)):
            if self.products[i].name == keyword:
                print(f"Товар під назвою {self.products[i].name} знайдено! Під номером {i+1}")
                return self.products[i]
        print(f"Твар не знайдено!")
        return None
class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product):
        self.cart.add_product(product)

    def checkout(self, cart : Cart):
        cart.show_card()
        total = cart.total_price()
        print(f"Загальна сума {total} грн")

        products = self.cart.products
        self.cart = Cart()

        return total, products

    def search_my_cart(self, keyword):
        return self.cart.find_product_by_name(keyword)


class DeliveryService:
    def deliver(self, customer):
        if len(customer.cart.products) == 0:
            print('Вам принести порожню коробку?')
            return
        print(f"Доставка на ім'я {customer.name}")
        customer.cart.show_cart()
        total = customer.cart.total_price()
        print(f"Загльна сума: {total} грн")


banana = FoodProduct("Banana", 100, "04.12.2025")
banana.get_info()
banana.apply_discount(30)
banana.new_expiration_date("04.13.2025")
banana.get_info()
laptop = Tehnic("Acer nitro V15", 35000, 0)
laptop.get_info()
cart1 = Cart()
cart1.show_card()
cart1.add_product(banana)
cart1.add_product(laptop)
cart1.show_card()
cart1.total_price()
cart1.remove_product(banana)
cart1.total_price()
cart1.show_card()
cart1.add_product(banana)
cart1.show_card()
cart1.total_price()
cart1.apply_discount_to_all(5)
cart1.total_price()
cart1.find_product_by_name("Acer nitro V15")
cart1.find_product_by_name("Banana")
d = Customer("Danylo")
d.add_to_cart(banana)
d.add_to_cart(laptop)
d.search_my_cart(cart1)
a = DeliveryService()
a.deliver(d)