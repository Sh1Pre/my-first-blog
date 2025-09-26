#l = []
#nm = int(input("Количество чисел: "))
#sm = 0
#for i in range(0, nm):
#    add = int(input(f"Введи {i+1} число: "))
#    l.append(add)

#i = 0

#for i in range(0, nm):
#    sm += l[i]
#    i += 1

#print("Сумма чисел:", sm)
#print("Содержимое списка:", l)
#n = int(input("Количество элементов в списке: "))
#l = []
#e = 1
#for i in range(n):
 #   e = int(input("Введите число: "))
#    if e != 0:
#        l.append(e)
#    else:
#        break
#if e == 0:
  #  print("Работа программы завершена")
 #   print("Содержимое списка: ", l)
 #   exit()
#else:
#    print("Содержимое списка: ", l)
#    exit()

#n2 = n1 // 100
#n3 = (n1 - (n2 * 100)) // 10
#n4 = (n1 - ((n3 * 10) + (n2 * 100))) // 1
#print(f"В числе {n2} сотен, {n3} десятков, {n4} единиц")

with open("hello.txt", "r+") as n1:
    n2 = n1.read()
    print(f"В этом числе {n2.count("2")} цифры \"2\" ")
    n1.close()

#dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
#words = [f"{key}: {dictionary[key]}" for key in dictionary if len(key) > 3]
#print(words)

#with open("hello.txt", "w+") as myfile:
#    print("Работа с файлом myfile")
#    myfile.write("39")
#    print("\n88", file=myfile)
#myfile.close()
#print("Закрытие")

#FILENAME = "hello.txt"


#def write():
#    message = input("Введите строку: ")
#    with open(FILENAME, "a") as file:
#        file.write(message + "\n")


#def read():
#    with open(FILENAME, "r") as file:
#        for message in file:
#            print(message, end="")
#    print()


#while True:
#    selection = int(input("1.Запись в файл\t\t2.Чтение файла\t\t3.Выход\nВыберите действие: "))
#    match selection:
#        case 1:
#            write()
#       case 2:
#            read()
#        case 3:
#           break
#        case _:
#            print("Некорректный ввод")

#print("Программа завершена")