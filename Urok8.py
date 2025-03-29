class Calculator:
    def divide(self, a,b):
        if b == 0:
            raise ZeroDivisionError
        return a/b

c = Calculator()
try:
    print(c.divide(6, 0))
except ZeroDivisionError:
    print("BOOOM!")