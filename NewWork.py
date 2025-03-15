class Student:
    def __init__(self, name = None, age = 0, grade = []):
        self.name = name
        self.age = age
        self.grade = grade
    def add_grade(self):
        self.grade.append(12)
        self.grade.append(12)
        self.grade.append(12)
        self.grade.append(11)
        self.grade.append(11)
        self.grade.append(11)
        print(self.grade)
    def get_avg(self):
        gfr = float(sum(self.grade) / len(self.grade))
        print(f"Середній бал: ", gfr)
c = Student()
c.add_grade()
c.get_avg()
