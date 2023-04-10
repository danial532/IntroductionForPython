# n = None #если знаем, что может понадобиться переменная
# print(n)
# n=5
# print(type(n)) #-вывод типа данных переменной
# n='sjhjhgjh'
# print(type(n))


#способы вывода переменных
# a = 5
# b = 5,89
# c = 'hello'
# print (a, ' - ', b, ' - ',c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))

# print('Введите первое число:') # ввод с новой строки 
# a = int(input())
# print(a)
# print(type(a))
# b = int(input('Введите второе число:')) # ввод как продолжение приглашения
# print (a, ' + ', b, ' = ', a + b)

# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

#c = round (a*b, 3) #округление по математическим правилам, 
# после запятой-количество знаков

# if condition:
#     # operator
# elif condition2:
#     # operator 2

# while condition:
#     # operator 1
# #operator 2

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i= i + 1
# else:
#     print('Пожалуй')
#     print ('хватит')
# print (i)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0 #если остаток от деления n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введнное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# for i in range(1,10, 2): #2 это на сколько увеличивать число
#     print(i)

# line = ""
# for i in range(3):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)