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
        for i in self.passengers:
            print(i.name)

obj1 = Human('Danylo')
obj2 = Human('Rozum')
buss1 = Buss()
buss1.addpassengers(obj1)
buss1.v()
buss1 = Buss()
buss1.addpassengers(obj2)
buss1.v()