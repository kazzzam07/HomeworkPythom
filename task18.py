# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

my_list = []
n = int(input("Введите колличество элементов в массиве: "))

for _ in range(n):
    my_list.append(randint(1, 50))
print(my_list)

x = int(input("Введите число Х: "))
num = 0
min_element = abs(x - my_list[0])

for i in range(0, n):
    buff_element = abs(x - my_list[i])
    if buff_element < min_element:
        min_element = buff_element
        num = i

print(my_list[num])

