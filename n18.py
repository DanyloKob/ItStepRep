class Bank:
    def __init__(self, balanse = 0):
        self.balanse = balanse
        if self.balanse <= 0:
            raise ValueError
    def withrawd(self, amount = 0):
        if amount > self.balanse:
            raise ValueError
        print(f"Ваш баланс: {self.balanse}, до знімання {amount}")
        self.balanse = self.balanse - amount
        print("Новий баланс: ", self.balanse)


try:
    c = Bank(3000)
    c.withrawd(300)
    c.withrawd(500)
    c.withrawd(2500)
except ValueError:
    print("Ну от, Ваш акаунт було видалено!")