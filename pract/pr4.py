#name = input("Введите ваше имя: ")
#print("Привет,", name)
#print(name,", Сколько тебе лет?")
#yo = input()

#n1 = int(input("Введите первое число: "))
#n2 = int(input("Введите второе число: "))
#print("Сумма: ", n1 + n2)
#print("Разность: ", n1 - n2)
#print("Умножение: ", n1 * n2)
#print("Деление: ", n1 / n2)

#P = int(input("Введите начальную сумму: "))
#R = int(input("Процент по вкладу: "))
#T = int(input("Количество лет: "))
#print("Начисленные проценты:", (P * R * T) / 100)

#C = int(input("Введите температуру в градусах Цельсия: "))
#print(C, "градусов Цельсия равны", (9 / 5) * C + 32, "градусам Фаренгейта")

#def select(input_func):
#    def output_func():
#        print("*****************")
#        input_func()
#        print("*****************")

#    return output_func
#

#@select
#def hello():
#   print("Hello METANIT.COM")


#hello()

#def check(input_func):
#    def output_func(*args):
#        input_func(*args)

#    return output_func
#

#@check
#def print_person(name, age):
#    print(f"Name: {name}  Age: {age}")


#print_person("Tom", 38)

#def check(input_func):
#    def output_func(*args):
#        name = args[0]
#        age = args[1]
#        if age < 0: age = 1
#        input_func(name, age)

#    return output_func


#@check
#def print_person(name, age):
#    print(f"Name: {name}  Age: {age}")


#print_person("Tom", 38)
#print_person("Bob", -5)

import time

#def check(input_func):
#    def output_func(*args):
#        result = input_func(*args)
#        if result < 0: result = 0
#        return result
#
#    return output_func


#@check
#def sum(a, b):
#    return a + b
#

#result1 = sum(10, 20)
#print(result1)
#time.sleep(1)
#result2 = sum(10, -20)
#print(result2)

#class Person:
#    def __init__(self, name, age):
#        self.__name = name
#        self.__age = age

#    def set_age(self, age):
#        if 0 < age < 110:
#            self.__age = age
#        else:
#            print("Недопустимый возраст")

#    def get_age(self):
#        return self.__age

#    def get_name(self):
#        return self.__name

#    def print_person(self):
#        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


#tom = Person("Tom", 39)
#tom.print_person()
#tom.set_age(-3486)
#tom.set_age(25)
#tom.print_person()

#class Person:
#   def __init__(self, name, age):
#       self.__name = name
#        self.__age = age

#    @property
#    def age(self):
#        return self.__age

#   @age.setter
#    def age(self, age):
#        if 0 < age < 110:
#            self.__age = age
#        else:
#            print("Недопустимый возраст")

#    @property
#    def name(self):
#        return self.__name

#    def print_person(self):
#        print(f"Имя: {self.__name}\tВозраст: {self.__age}")

#
#tom = Person("Tom", 39)
#tom.print_person()
#tom.age = -3486
#print(tom.age)
#tom.age = 25
#tom.print_person()

#class Person:

#    def __init__(self, name):
#        self.__name = name

#    @property
#    def name(self):
#        return self.__name

#    def display_info(self):
#        print(f"Name: {self.__name} ")


#class Employee(Person):

#    def work(self):
#        print(f"{self.name} works")


#tom = Employee("Tom")
#print(tom.name)
#tom.display_info()
#tom.work()

class Employee:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def work(self):
        print(f"{self.name} works")


class Student:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def study(self):
        print(f"{self.name} studies")


class WorkingStudent(Employee, Student):
    pass


tom = WorkingStudent("Tom")
tom.work()  # Tom works
tom.study()  