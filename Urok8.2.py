class Product:
    def __init__(self, name = None, prise = 0, quantity = 0, amoun = 0):
        self.amoun = amoun
        self.name = name
        self.prise = prise
        self.quantity = quantity
        if self.prise < 0:
            raise ValueError
        if self.quantity < 0:
            raise ValueError
    def buy(self, amount = 1):
        if amount > self.amoun:
            raise ValueError
        self.amoun = self.amoun - amount
        print("Сума:", self.prise * amount)
    def apply_discount(self, discount = 0, amount = 0):
        if discount > 100 or discount < 0:
            raise ValueError
        self.amoun = self.amoun - amount
        dis = discount/100
        disr = 1 - dis
        print("Сума:", self.prise * amount * disr, "знишка: ", discount, "%")
try:
    obj = Product("Торт", 100, 1, 15)
    obj.apply_discount(10, 10)
    obj.buy(6)
except ValueError:
    print('Магазину більше нема, ЧЕРЕЗ ВАС!')

try:
    obj = Product("Чай", 1000, 10, 5)
    obj.apply_discount(90, 3)
    obj.buy(2)
except ValueError:
    print('Магазину більше нема, ЧЕРЕЗ ВАС!')