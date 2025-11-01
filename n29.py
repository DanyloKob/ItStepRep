from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    def get_info(self):
        print(f"Ім'я: {self.name}, вік: {self.age}")


class Dog(Animal):
    def make_sound(self):
        print("Гав-гав!")


class Cat(Animal):
    def make_sound(self):
        print("Няв-няв!")


class Parrot(Animal):
    def make_sound(self):
        print("Привіт!")


dog = Dog("Я забув як звати собаку сусідки", 3)
cat = Cat("Боже, я вже не можу придумати імена...", 2)
parrot = Parrot("Хмммммм ПОМОЖІТЬ!!!", 5)
dog.make_sound()
dog.get_info()
cat.make_sound()
cat.get_info()
parrot.make_sound()
parrot.get_info()