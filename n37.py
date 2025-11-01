print("ГРА")
print("Вгадай інградієнти у піці від Мікіланджо")
print("Хочеш вгадати інградієнти? Спробуйте!!!")


import random

# Налаштування гри
NUM_PICKS = 7         # кількість інгредієнтів у замовленні
ATTEMPT_COST = 2      # скільки енергії витрачається за одну спробу
REWARD_PER_MATCH = 3  # скільки балів за один збіг

print(f'Кількість інградієнтів: {NUM_PICKS}')
print(f'Кількість енергії/спробу: {ATTEMPT_COST}')
print(f'Кількість балів/спробу: {REWARD_PER_MATCH}')

# Список доступних топінгів (інгредієнтів)
TOPPINGS = [
    "сир", "пепероні", "гриби", "оливки", "ананас", "кукурудза", "перець",
    "цибуля", "шинка", "томати", "бекон", "базилік", "чилі", "моцарела",
    "шпинат", "курка", "соус BBQ", "соус песто", "артишок", "чесник"
]

# Стартові значення
energy = 10     # стартова енергія
score = 0       # стартові бали
rP = []
rM = []
check = 1

print(f'Кількість енергії: {energy}')


while True:
    check = int(input('1 - грати, 0 - не грати.'))
    if check == 0:
        break
    for i in range(NUM_PICKS):
        ranP = random.choice(TOPPINGS)
        rM.append(ranP)
    m = input().split()
    for i in range(len(m)):
        rP.append(m[i])
    print(f'for devs: rp={rP} rm={rM}')
    for n in rP:
        if energy >= ATTEMPT_COST:
            energy -= ATTEMPT_COST
            if n in rM:
                score += REWARD_PER_MATCH
                print(f"{n}- ВГАДАЛИ!!! +{REWARD_PER_MATCH}балів, баланс: {score}")
                rM.remove(n)
            else:
                print(f"{n}- НЕ ВГАДАЛИ, LOL")
        else:
            print(f"Нема енергії! Нємощ! потрібно {ATTEMPT_COST}")
    print(f'Ви отримали: {score}')

print("Гру закінчено!")