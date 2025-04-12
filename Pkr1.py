from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def info(self):
        pass

    def Print(self):
        print('Hi')

class Tehnic(Product):
    def __init__(self, name, prise, waranty):
        super().__init__(name, prise)
        self.waranty = waranty

    def info(self):
        print(self.name, self.price, self.waranty)

    def set_waranty(self, w):
        self.waranty = int(w)

class Fruct(Product):
    def __init__(self, name, prise, endday):
        super().__init__(name, prise)
        self.endday = endday

    def info(self):
        print(self.name, self.price, self.endday)

class Cart:
    def __init__(self):
        self.cart = []

    def addtocard(self, obj: Product):
        self.cart.append(obj)

    def PrintCard(self):
        print(self.cart)

c = Tehnic(1,1,1)
c.info()
c.set_waranty(10)
