class Human:
    def __init__(self, name = None):
        self.name = name
    def setname(self, name):
        self.name = name

class Auto:
    def __init__(self):
        self.pas = []

    def addpas(self, human: Human):
        self.pas.append(human)

    def v(self):
        print(self.pas)

obj = Human('Danylo')
Audi = Auto()
Audi.addpas(obj)
Audi.v()