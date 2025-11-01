def calculator(a, b, c):
    try:
        if c == "+":
            print(a + b)
        elif c == "-":
            print(a - b)
        elif c == "*":
            print(a * b)
        elif c == "/":
            try:
                print(a / b)
            except ZeroDivisionError:
                print("b is 0")
                b = 1
                print("a/1: ", a / b)
    except ValueError:
        print("Error, plz write only number!")

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

try:
    c = input("Введіть операцію: ")
    if c != {"+", "-", "*", "/"}:
        raise ValueError
except ValueError:
    print("Ви можете вводити операції тільки: +, -, *, / !!!")

print(calculator(a, b, c))
