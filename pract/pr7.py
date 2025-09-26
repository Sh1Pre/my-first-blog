#w = input("Введите предложение: ")
#n = w.replace(" ", "_")
#print("Замененный текст:", n)

#import abc


#class Shape(abc.ABC):
#    @abc.abstractmethod
#    def area(self): pass



#class Rectangle(Shape):
#    def __init__(self, width, height):
#        self.width = width
#        self.height = height

#    def area(self): return self.width * self.height



#class Circle(Shape):
#    def __init__(self, radius):
#        self.radius = radius

 #   def area(self): return self.radius * self.radius * 3.14


#def print_area(shape):
#    print("Area:", shape.area())


#rect = Rectangle(30, 50)
#circle = Circle(30)
#print_area(rect)
#print_area(circle)

#import abc


#class Shape(abc.ABC):
#    def __init__(self, x, y):
#        self.x = x
 #       self.y = y

#    @abc.abstractmethod
#    def area(self): pass

#    def print_point(self):
#       print("X:", self.x, "\tY:", self.y)


#class Rectangle(Shape):
#    def __init__(self, x, y, width, height):
#       super().__init__(x, y)
#        self.width = width
#        self.height = height

#    def area(self): return self.width * self.height


#rect = Rectangle(10, 20, 100, 100)
#rect.print_point()

#try:
#    number1 = int(input("Введите первое число: "))
#    number2 = int(input("Введите второе число: "))
#    print("Результат деления:", number1/number2)
#except ValueError:
#    print("Преобразование прошло неудачно")
#except ZeroDivisionError:
#    print("Попытка деления числа на ноль")
#except BaseException:
#    print("Общее исключение")
#print("Завершение программы")

#class PersonAgeException(Exception):
#    def __init__(self, age, minage, maxage):
#        self.age = age
#        self.minage = minage
#        self.maxage = maxage

#    def __str__(self):
 #       return f"Недопустимое значение: {self.age}. " \
#               f"Возраст должен быть в диапазоне от {self.minage} до {self.maxage}"


#class Person:
#    def __init__(self, name, age):
#        self.__name = name
#        minage, maxage = 1, 110
#        if minage < age < maxage:
#            self.__age = age
#        else:
#            raise PersonAgeException(age, minage, maxage)

#   def display_info(self):
#        print(f"Имя: {self.__name}  Возраст: {self.__age}")


#try:
#    tom = Person("Tom", 37)
#    tom.display_info()
#
#    bob = Person("Bob", -23)
#    bob.display_info()
#except PersonAgeException as e:
#    print(e)

#numbers = []
#n1 = int(input("Количество чисел: "))
#n2 = 0
#i = 0
#while i < n1:
#    numbers.append(int(input("Введите число: ")))
#    i += 1
#i = 0
#while i < len(numbers):
#    n2 += numbers[i]
#    i += 1
#print("Среднее арифметическое:", n2 / len(numbers))
import time
import os

print("in", flush=True)
time.sleep(0.2)
print("in a", flush=True)
time.sleep(0.2)
print("in a lu", flush=True)
time.sleep(0.2)
print("in a lucid", flush=True)
time.sleep(0.2)
print("in a lucid pa", flush=True)
time.sleep(0.2)
print("in a lucid para", flush=True)
time.sleep(0.2)
print("in a lucid paradise", )
time.sleep(0.2)