# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.
# Пример:
# Ввод: 13 -> 1, 2, 4, 8
c = 1
k = 1
N = int(input('Введите число N: '))
while c <= N:
    c = 2 ** k
    print(c)
    k += 1
