#class Person:

#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def say_hello(self):
#        print("Hello")

#class Car:

#   def __init__(self, brand, color, speed):
#       self.brand = brand
#       self.color = color
#        self.speed = speed

#    def drive(self):
#        self.speed = 60
#        print("Car moving")

#   def stop(self):
#        self.speed = 0
#        print("Car stop")

#car1 = Car("bmw", "blue", 0)

#print(car1.brand, car1.color)
#car1.drive()
#print(car1.speed)
#car1.stop()
#print(car1.speed)

#tom = Person("Tom", 22)

#print(tom.name)
#print(tom.age)
#tom.age = 37
#print(tom.age)
#tom.company = "Microsoft"
#print(tom.company)
#tom.say_hello()

#class Rectangle:

#   def __init__(self, length, width):
#        self.length = length
#        self.width = width

#   def perimeter(self):
#        P = (self.length + self.width) * 2
#        print("Периметр прямоугольника:", P)

#    def area(self):
#        S = self.length * self.width
#        print("Площадь прямоугольника:", S)

#rt1 = Rectangle(10, 5)
#rt2 = Rectangle(11, 39)
#rt1.perimeter(), rt1.area()
#print(" ")
#rt2.perimeter(), rt2.area()

#import time

#class BankAccount:

#    def __init__(self, account_number, balance):
#        self.account = account_number
#        self.balance = balance

#    def add(self):
#        add = int(input("Введите сумму для пополнения: "))
#        self.balance += add
#       print("Деньги успешно зачислены на счет")
#        time.sleep(1)
#        print("Текущий баланс:", self.balance)
#        time.sleep(1)

#   def withdraw(self):
#       wd = int(input("Введите сумму для снятия: "))
#        if self.balance >= wd:
#            self.balance -= wd
#            print("Деньги успешно сняты")
#            time.sleep(1)
#        else:
#            print("Недостаточно средств на балансе")
#        print("Текущий баланс:", self.balance)

#user1 = BankAccount(39, 50000)
#user1.add()
#user1.withdraw()
#print("Выход из программы...")

names = ["Tom", "Bob", "Sam"]
ages = [41, 46, 35]

users = list(zip(names, ages))
print(users)

for user in users:
    print(user)
