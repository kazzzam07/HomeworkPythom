# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

my_list = []
n = int(input("Введите колличество элементов в массиве: "))

for _ in range(n):
    my_list.append(randint(0, 10))
print(my_list)

x = int(input("Введите число Х: "))
count = 0
for i in range(len(my_list)-1):
    if my_list[i] == x:
        count += 1
print(count)