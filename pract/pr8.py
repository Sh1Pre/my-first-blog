a = int(input("Количество чисел: "))
n1 = 0
l = []
lp = []
ln = []

for i in range(a):
    add = int(input(f"Введите {i+1} элемент: "))
    l.append(add)

i = 0

for i in range(a):
    n1 += l[i]
    i +=1

i = 0

for i in range(a):
    if l[i] >= 0:
        lp.append(l[i])
    else:
        ln.append(l[i])

print("Содержимое списка:", l)
print("Минимальный элемент:", min(l))
print("Максимальный элемент:", max(l))
print("Среднее арифметическое:", n1 / len(l))
print("Положительных чисел:", len(lp))
print("Отрицательных чисел:", len(ln))
