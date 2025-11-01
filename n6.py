class Book:
    def __init__(self, title=None, author=None):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def addBook(self, b: Book):
        self.books.append(b)

    def v(self):
        for i in self.books:
            print(i.title, i.author)

    def removeBook(self, b: Book):
        self.books.remove(b)


obj1 = Book("Кобзар", "Тарас Шевченко")
obj2 = Book("Кобзар 2", "Тарас Шевченко")
library1 = Library()
library1.addBook(obj1)
library1.v()
library1.addBook(obj2)
library1.v()
library1.removeBook(obj1)
library1.v()