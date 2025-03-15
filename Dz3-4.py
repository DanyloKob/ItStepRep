class Counter:
    def __init__(self, count=0):
        self.count = 0

    def increment(self):
        self.count = self.count + 1
        print(f"Ось Ваш рахунок після додавання: {self.count}")

    def decrement(self):
        self.count = self.count - 1
        print(f"Ось Ваш рахунок після віднімання: {self.count}")

    def reset(self):
        self.count = 0
        print(f"Онулено! Хахахахахахахахахахаах: {self.count}")

c = Counter()
c.increment()
c.decrement()
c.reset()
c.decrement()
c.reset()
c.decrement()
c.reset()
c.increment()
c.decrement()
c.reset()
c.decrement()
c.reset()
c.increment()
c.decrement()
c.increment()
c.increment()
c.increment()
c.increment()
c.decrement()
c.reset()