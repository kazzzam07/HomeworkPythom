# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Ввведите трехзначное число: "))

if number > 99 and number < 1000:
    digit1 = number % 10
    number = number//10
    digit2 = number % 10
    number = number//10
    sum = number + digit1 + digit2
    print(f'Сумма чисел трехзначного числа равна: {sum}')

else:
    print("Число не трехзначное !")

