try:
    acc = float(input("Ваш баланс в грн: "))
    if acc < 0:
        raise ValueError
    v = str(input("В яку валюту перевести: "))
    if v == 'USD':
        print("Ваш баланс в USD: ", acc / 41.48)
    elif v == 'EUR':
        print("Ваш баланс в EUR: ", acc / 44.68)
    elif v == 'GBP':
        print("Ваш баланс в GBP: ", acc / 53.63)
    else:
        raise ValueError
except ValueError:
    print("Ваш баланс не має бути від'ємний та переводьте в існуючі валюти банку!")

