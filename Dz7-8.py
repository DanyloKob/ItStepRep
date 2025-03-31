class Calculator:
    def __init__(self, a, b):
        try:
            self.a = float(a)
            self.b = float(b)
        except ValueError:
            raise TypeError("Не знаю чому тип помилка якщо за букви інша помилка відповідаю._.")

    def summmmma(self):
        return self.a + self.b

    def vidnimanna(self):
        return self.a - self.b

    def mnoz(self):
        return self.a * self.b

    def dil(self):
        if self.b == 0:
            raise ZeroDivisionError
        return self.a / self.b


try:
    calc = Calculator(10, 5)
    print(calc.summmmma())
    print(calc.vidnimanna())
    print(calc.mnoz())
    print(calc.dil())
    calc0 = Calculator(10, 0)
    calc0.dil()
    calc0 = Calculator("a", 10)
    calc0.dil()
except ZeroDivisionError:
    print("Точно курва якщо ділиш на нуль, шо тоді, нескінченно казати чи шо?")
except TypeError:
    print("Нє но курва написав не числа, ТІЛЬКИ ЧИСЛА! Або ше якась помилка")