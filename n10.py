class Coleso:
    def Rotate(self):
        print("Rotating")

class Rama:
    def Conect(self):
        print("Conecting")

class Bike(Coleso, Rama):
    pass

b = Bike()
b.Rotate()
b.Conect()
