# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

num = int(input("Введите число: "))
sqr = 1
i = 0

while sqr <= num:
    print(sqr, end=" ")
    i += 1
    sqr = 2**i

    