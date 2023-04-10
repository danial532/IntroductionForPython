# Task2 Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print('Введите трехзначное число')
number = (input())
if len(number) != 3:
    print('это не трехзначное число')
else:
    n1 = int(number[0])
    n2 = int(number[1])
    n3 = int(number[2])
    print(f"{number[0]} + {number[1]} + {number[2]} = {n1+n2+n3}")
