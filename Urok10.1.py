from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand = None):
        self.brand = brand

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def info(self):
        pass

class Car(Vehicle):
    def drive(self):
        print(f"Машина їде, колеса труться...")
    def info(self):
        print(f"Бренд: {self.brand}")

class Bike(Vehicle):
    def drive(self):
        print(f"Ровер їде, колеса труться...")

    def info(self):
        print(f"Бренд: {self.brand}")

c = Car("Idk")
b = Bike("Idk2")
c.drive()
b.drive()
c.info()
b.info()