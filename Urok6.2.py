class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def info(self):
        print(f"Бренд: {self.brand}. Максимальна швидкість: {self.speed}.")


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def info(self):
        super().info()
        print(f"Тип палбного: {self.fuel_type}")


vehicle = Vehicle("Данило-Бренд", 800)
vehicle.info()
car = Car("Спід-Данило-Бренд", 801, "Газ!")
car.info()