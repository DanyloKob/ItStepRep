try:
    a = int(input())
    b = int(input())
    print(a/b)
except ZeroDivisionError:
    print("b is 0")
    b = 1
    print("a/1: ", a/b)
except ValueError:
    print("Error, plz write only number!")
