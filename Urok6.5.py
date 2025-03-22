class Car:
    def drive(self):
        print("The car is driving")
class Plane:
    def fly(self):
        print("The plane is flying")
class FlyingCar(Car, Plane):
    def show_abilites(self):
        super().drive()
        super().fly()

a = FlyingCar()
a.show_abilites()