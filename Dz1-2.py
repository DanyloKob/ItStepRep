def calculator(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        if b == 0:
            return "НАЙ ДІЛИТИ НА НУЛЬ!!!"
        return a / b
    else:
        return "Я не вмію таке робити:("

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = input("Введіть операцію: ")
print(calculator(a, b, c))
