class Customer:
    def __init__(self, name=None, phone=None):
        self.name = name
        self.phone = phone


class MenuItem:
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price


class Order:
    def __init__(self, customer: Customer):
        self.customer = customer
        self.items = []

    def add_item(self, menu_item: MenuItem):
        self.items.append(menu_item)

    def get_total(self):
        all = 0
        for item in self.items:
            all += item.price
        return all

    def show_order(self):
        print(f"Клієнт: {self.customer.name}, Телефон: {self.customer.phone}")
        for item in self.items:
            print(f"{item.name} - {item.price} грн")
        print(f"Загальна сума: {self.get_total()} грн")


customer1 = Customer("Кобзар Данило", "+380935120853")
item1 = MenuItem("Лате ГІГАНСЬКЕ", 3000)
item2 = MenuItem("Булочка з маком", 35)
order1 = Order(customer1)
order1.add_item(item1)
order1.add_item(item2)
order1.show_order()