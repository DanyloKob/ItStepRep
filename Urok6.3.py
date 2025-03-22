class Water:
    def Swim(self):
        print("You can swim")

    def Walk(self):
        print("To to to")

class Ground:
    def Walk(self):
        print("You can walk")

class Amfibia(Water, Ground):
    pass

b = Amfibia()
b.Swim()
b.Walk()
