from abc import ABC, abstractmethod

sp = []
class PaymentMethod(ABC):
    def __init__(self, amount=0):
        self.amount = amount



    @abstractmethod
    def pay(self):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self):
        if self.amount <= 0:
            raise ValueError
        print(f"Ви віддали нам {self.amount} грн. ОПЛАТА КАРТОЮ 05.04.2025")
        sp.append(f"ОПЛАТА КАРТОЮ 05.04.2025 | СУМА: {self.amount} грн")

class CryptoPayment(PaymentMethod):
    def pay(self):
        if self.amount <= 0:
            raise ValueError
        print(f"Ви віддали нам {self.amount} грн. ОПЛАТА КРИПТОЮ 05.04.2025")
        sp.append(f"ОПЛАТА КРИПТОЮ 05.04.2025 | СУМА: {self.amount} грн")
def log():
    print(f"Ось Ваші оплати: {sp}")
a = CreditCardPayment(1001)
b = CryptoPayment(2012)
try:
    a.pay()
    b.pay()
except ValueError:
    print("Хахахахах Ви не здатні забрати у нас гроші!")
try:
    log()
except:
    print("помилка")
try:
    a.pay()
    b.pay()
except ValueError:
    print("Хахахахах Ви не здатні забрати у нас гроші!")
try:
    log()
except:
    print("помилка")