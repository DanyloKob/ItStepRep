class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.sound}")


class Dog(Animal):
    def __init__(self, name, sound="Гав"): # я думав де вписати звук, вирішив шо можна тупо тут!
        super().__init__(name, sound)

    def make_sound(self):
        super().make_sound()
        print(f"Я {self.name}!")


class Cat(Animal):
    def __init__(self, name, sound="Мяу"): # я думав де вписати звук, вирішив шо можна тупо тут!
        super().__init__(name, sound)

    def make_sound(self):
        super().make_sound()
        print(f"Я {self.name}!")


dog = Dog("Собакен")
cat = Cat("Котя")
dog.make_sound()
cat.make_sound()

# більше не пишіть таких складних умов._.