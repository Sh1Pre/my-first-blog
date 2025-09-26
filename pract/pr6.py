#password = "1234"
#checkpassword = input("Введите пароль: ")

#if password == checkpassword:
#    print("Вход выполнен")
#else:
#    print("Неверный пароль")

#n1 = int(input("Введите число: "))
#for n2 in range(1, 10):
#    print(n1, "*", n2, "=", n1 * n2)

#buf = 0
#n1 = int(input("Введите число: "))
#for n2 in range(1, n1 + 1):
#    buf += n2
#print("S =", buf)

import random
import time

#n1 = random.randint(1, 100)
#n2 = 0

#while not n2 == n1:
#    n2 = int(input("Введите число: "))
#    if n2 > n1:
#        print("Неправильно, число меньше", n2)
#        time.sleep(1)
#    elif n2 < n1:
#        print("Неправильно, число больше", n2)
#        time.sleep(1)
#else:
#    print("Правильно, загаданное число было", n1)
#    time.sleep(1)

#text = input("Введите предложение: ")
#words = text.count(" ") + 1
#print("Слов в предложении:", words)

#min = int(input("Введите минуты: "))

#hours = min // 60
#lmin = min % 60

#print(hours, "часов,", lmin, "минут")

#text = input("Введите предложение: ")
#repltext = text.replace(" ", "_")
#print(repltext)

list = [1, -5, 5, 23, 54, -43, -12, 39]
plist = []
mlist = []

if list[0:7] > 0:
