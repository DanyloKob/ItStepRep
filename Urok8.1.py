class Person:
    def __init__(self, age = 1):
        self.age = age
        if self.age > 120 or self.age < 0:
            raise ValueError


p = Person()
try:
    ager = int(input())
    print(p.perevirca(ager))
except ValueError:
    print("BOOOM!")