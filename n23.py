from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, par1 = 0, par2 = 0):
        self.par1 = par1
        self.par2 = par2

    @abstractmethod
    def calcArea(self):
        pass


class Triangle(Shape):
    def calcArea(self):
        print(0.5*self.par1*self.par2)

class Sircle(Shape):
    def calcArea(self):
        print(self.par1**2 * self.par2)

f = Triangle(4, 6)
c = Sircle(4, 3.14)
f.calcArea()
c.calcArea()