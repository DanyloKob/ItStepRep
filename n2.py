class Cow:
    def __init__(self, name = None, age = 0):
        self.name = name
        self.age = age
    def Info(self):
        print(f'Name is {self.name}. Age is {self.age}.')
    def Moo(self):
        print("Mooo moo!")
co = Cow("Cooow", 5)
# co.Moo()
# co.Info()
# co.Moo()

class Triangle:
    def __init__(self, long = 0, weight = 0, height = 0):
        self.long = long
        self.weight = weight
        self.height = height

    def Info(self):
        print(f'Long is {self.long}. Weight is {self.weight}. Height is {self.height}.')

    def CalcArea(self):
        s = self.weight * self.height * 0.5
        print(f"Scale is {s}")
    def CalcArea2(self):
        p = self.weight + self.long + self.long
        print(f"Scale is {p}")


cor = Triangle(10, 20, 15)
# cor.Info()
# cor.CalcArea()
# cor.CalcArea2()

class BankAcc:
    def __init__(self, owner='Власник', balance=0):
        self.owner = owner
        self.balance = balance
    def deposite(self, amount1):
        self.balance = self.balance + amount1
        print("Баланс: ", self.balance)
    def withdraw(self, amount2):
        if self.balance > amount2:
            self.balance = self.balance - amount2
        else:
            print("На вашому рахунку недостатньо коштів!")
        print("Баланс: ", self.balance)
cb = BankAcc()
# cb.deposite(120)
# cb.withdraw(500)
# cb.deposite(450)
# cb.withdraw(500)
print("HELLO?!!!")
