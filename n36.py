potions = ["зцілення", "сила", "манна", "невидимість"]
prices = {
    "зцілення": 15,
    "сила": 20,
    "манна": 10,
    "швидкість": 25
}
wish = ["манна", "невидимість", "зцілення", "сила"]
coins = 30
c = coins
bag = []

print("ПОЧИНАЄМО")
print("Купуємо все!")


for i in wish:
    if i in prices:
        if coins >= prices[i]:
            coins -= prices[i]
            bag.append(i)
            print(f"Вам вистачило грошей і ви купите: {i}, залишок: {coins}")
        else:
            print(f"Вам не вистачило грошей і ви не купите: {i}, залишок: {coins}, а потрібно {prices[i]}")
    else:
        print(f'От дє ви тако побачили "{i}"? ідіте звідсіля!!!')

print("")
print("ЧЕК")
for n in bag:
    if n in prices:
        print(f'"{n}" - {prices[n]}')
print(f"СУМА: {c - coins}")
print(f"ЗАЛШ: {coins}")