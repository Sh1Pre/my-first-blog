#a = 5
#b = 4
#result = a == b
#print(result)
#print(a != b)
#print (a != b)
#print(a > b)
#print(a < b)

#bool1 = True
#bool2 = False
#print(bool1 == bool2)

#age = 23
#weight = 58
#result = age > 21 and weight == 58
#print(result)

#age = 22
#isMarried = True
#print(not age > 21)
#print(not isMarried)

#message = "hello world"
#print("hello" not in message)
#print("gold" not in message)

#language = "1"
#if language == "english":
#    print("Hello")
#elif language == "russian":
#    print("Привет")
#else:
#    print("none")
#print("End")

#year = int(input("Введите год: "))
#if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#   print("Год високосный")
#else:
#    print("Год не високосный")

#a = int(input("Введите число a: "))
#b = int(input("Введите число b: "))
#if a > b:
#    print("Наибольшее число:", a)
#elif a < b:
#    print("Наибольшее число:", b)
#elif a == b:
#    print("Числа равны")
#else:
#    print("Введите нормальные числа")

#s = int(input("Введите сумму продажи: "))
#if 0 < s < 5000:
#    m = s / 100 * 5
#elif 5000 < s < 15000:
#    m = s / 100 * 12
#elif 15000 < s < 25000:
#    m = s / 100 * 20
#elif 25000 < s:
#    m = s / 100 * 30
#else:
#    print("Некорректная сумма")
#    quit()
#print("Скидка:", m)
#print("Сумма с учетом скидки:", s - m)

#number = 1

#while number < 10:
#    print(f"number = {number}")
 #   number += 1
#else:
#   print(f"number = {number}. Работа цикла завершена")
#print("Работа программы завершена")

#import random
#win = True
#b = random.randint(1, 6)
#while win := True:
#    a = int(input("Введите число: "))
#    if a == b:
#        win = False
#        print("+")
#        quit()
#    else:
#        win = True
#        print("-")

#message = "Hello"
#for c in message:
#    print(c)
#else:
#    print(f"Последний символ: {c}. Цикл завершен")
#print("Работа программы завершена")

#while True:
#    a = int(input("Введите первое число: "))
#    b = int(input("Введите второе число: "))
#    c = a + b
#    print("Сумма чисел:", c)
#    e = input("Нажмите Y для завершения программы: ")
#    if e == "Y" or e == "y": break

#n = 7
#for i in range(0, n):
#    for j in range(0, n):
#        if(i == 0 or i == n-1 or j==i or j == n-i-1): print("*", end="")
#        else: print(" ", end="")
#    print()

#h = 7
#w = h + 2
#m = w //4
#for i in range(1, h+1):
#    if (i <= m):
#        print(" " * (m-i) + "*" * (2*i) + " " * (w-2*i-2*m) + "*" *(2*i) + " " * (m-i))
#    else:
#      print(" " * (i - 2*m+1) + "*" * (w-2*(i-2*m+1)) + " " * (i - 2*m+1))

#n=5
#k=1
#counter=1
#for i in range(n):
#    for j in range(n):
#        if k % 2 == 0:
#

print(counter, end ="  ")
#            counter+=1
#        else: print("*",end="  ")
#        k+=1
#    print()