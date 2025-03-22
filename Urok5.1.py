class Human:
    def __init__(self, name = None, age = 0):
        self.name = name
        self.age = age
    def setname(self, name):
        self.name = name
    def setage(self, age):
        self.age = age

class Buss:
    def __init__(self, passengers = None):
        self.passengers = []

    def addpassengers(self, human: Human):
        self.passengers.append(human)

    def v(self):
        print(self.passengers)

obj = Human('Danylo')
buss1 = Buss()
buss1.addpassengers(obj)
buss1.v()
buss1 = Buss()
buss1.addpassengers(obj)
buss1.v()