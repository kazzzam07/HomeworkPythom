# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

count_coins = int(input("Введите количество монет: "))
coins = 1
coins_0 = 0
coins_1 = 0

for i in range(count_coins):
    coins = randint(0, 1)
    print(coins)

    if coins == 0:
        coins_0 += 1
    else:
        coins_1 += 1
# print(coins_0, coins_1)

if coins_0 >= coins_1:
    print(f'Минимальное количество монеток {coins_1}')
else:
    print(f'Минимальное количество монеток {coins_0}')
    





