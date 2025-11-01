class Build:
    def __init__(self, year, size):
        self.year = year
        self.size = size

    def printBuild(self):
        print(f"Year - {self.year}. Size - {self.size}")

class School(Build):
    def __init__(self, year, size, students):
        super().__init__(year, size)
        self.students = students

    def printBuild(self):
        super().printBuild()
        print(f"Student - {self.students}")

school = School(1920, 5, 1000)
shop = Build(2010, 2)
school.printBuild()
shop.printBuild()