class Human:
    def __init__(self, name = None, age = 0):
        self.name = name
        self.age = age
    def talk(self):
        print(f"Привіт! Я людина")
    def printInfo(self):
        print(f"Май нейм - {self.name}. Мені {self.age} років, я старий(!")

class Taxist(Human):
    def __init__(self, name=None, age=0, perekus=12):
        super().__init__(name, age)
        self.perekus = perekus
    def talk(self):
        print(f"Привіт! Я людина-таксист")
    def printInfo(self):
        print(f"Май нейм - {self.name}. Мені {self.age} років, я старий(! І у мене перекус О {self.perekus} годині дня!")
    def work(self):
        print(f"Пора працювати")

human = Human("Danylo", 14)
human.talk()
human.printInfo()
taxist = Taxist("Петро", 50, 16)
taxist.talk()
taxist.printInfo()
taxist.work()
