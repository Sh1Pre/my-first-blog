#def say_hello():
#    print("Hello")
#
##
#def say_goodbye():
#    print("Good Bye")
#

#say_hello()
#say_goodbye()

#def print_messages():
#    def say_hello(): print("Hello")
#    def say_goodbye(): print("Good Bye")
#    say_hello()
#    say_goodbye()
#
#
#print_messages()

#def main():
#    say_hello()
#    say_goodbye()
#

#def say_hello():
#    print("Hello")
#

#def say_goodbye():
#    print("Good Bye")
#

#main()

#def print_person(name, age):
#    print(f"Name: {name}")
#    print(f"Age: {age}")
#

#print_person("N", 20)

#def print_person(name, *, age, company):
#    print(f"Name: {name}  Age: {age}  Company: {company}")
#

#print_person("Bob", age=41, company="Microsoft")

#def sum(*numbers):
#    result = 0
#    for n in numbers:
#        result += n
#    print(f"sum = {result}")
#

#sum(1, 2, 3, 4, 5)  # sum = 15
#sum(3, 4, 5, 6)  # sum = 18

#def double(number):
#    return 2 * number
#
#
#result1 = double(4)
#result2 = double(5)
#print(f"result1 = {result1}")
#print(f"result2 = {result2}")

#def print_person(name, age):
#    if age > 120 or age < 1:
#        print("Invalid age")
#        return
#    print(f"Name: {name}  Age: {age}")
#

#print_person("Tom", 22)
#print_person("Bob", -102)

#def sum(a, b): return a + b
#

#def multiply(a, b): return a * b
#

#operation = sum
#result = operation(5, 6)
#print(result)

#operation = multiply
#print(operation(5, 6))

#def do_operation(a, b, operation):
#    result = operation(a, b)
#    print(f"result = {result}")
#

#def sum(a, b): return a + b
#

#def multiply(a, b): return a * b
#

#do_operation(5, 4, sum)
#do_operation(5, 4, multiply)

#def sum(a, b): return a + b


#def subtract(a, b): return a - b


#def multiply(a, b): return a * b
#

#def select_operation(choice):
#    if choice == 1:
#        return sum
  #  elif choice == 2:
 #       return subtract
#    else:
#        return multiply
#

#operation = select_operation(1)
#print(operation(10, 6))

#operation = select_operation(2)
#print(operation(10, 6))

#operation = select_operation(3)
#print(operation(10, 6))

#def select_operation(choice):
 #   if choice == 1:
 #       return lambda a, b: a + b
 #   elif choice == 2:
 #       return lambda a, b: a - b
 #   else:
 #       return lambda a, b: a * b


#operation = select_operation(1)
#print(operation(10, 6))

#operation = select_operation(2)
#print(operation(10, 6))

#operation = select_operation(3)
#print(operation(10, 6))

#name = "Tom"


#def say_hi():
#    global name
#    name = "Bob"
#    print("Hello", name)


#def say_bye():
#    print("Good bye", name)


#say_hi()
#say_bye()

#def outer():
#    n = 5

#    def inner():
#        nonlocal n
#        n = 25
#        print(n)

#    inner()
#    print(n)
#

#outer()

#def outer():
#    n = 5

#    def inner():
#        nonlocal n
#        n += 1
#        print(n)

#    return inner


#fn = outer()
#fn()
#fn()
#fn()

#def select(input_func):
   # def output_func():
  #      print("*****************")
 #       input_func()
#        print("*****************")

#    return output_func
#

#@select
#def hello():
 #   print("Hello METANIT.COM")


#hello()

#def check(input_func):
#    def output_func(*args):
#        result = input_func(*args)
#        if result < 0: result = 0
#        return result

 #   return output_func


#@check
#def sum(a, b):
#    return a + b


#result1 = sum(10, 20)
#print(result1)

#result2 = sum(10, -20)
#print(result2)

#class Person:

 #   def __init__(self, name, age):
 #       self.name = name
 #       self.age = age


#tom = Person("Tom", 22)
#bob = Person("Bob", 43)

#print(tom.name, tom.age)
#print(bob.name, bob.age)

#class Person:
#
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def display_info(self):
#        print(f"Name: {self.name}  Age: {self.age}")


#tom = Person("Tom", 22)
#tom.display_info()

#bob = Person("Bob", 43)
#bob.display_info()

#class Person:

 #   def __init__(self, name):
 #       self.name = name
 #       print("Создан человек с именем", self.name)

 #   def __del__(self):
 #       print("Удален человек с именем", self.name)
#

#def create_person():
#    tom = Person("Tom")


#create_person()
#print("Конец программы")

#class Rectangle:

 #   def __init__(self, width, length):
 #       self.width = width
 #       self.length = length

 #   def perimeter(self):
 #       p = self.width + self.length
 #       return p

 #   def area(self):
 #       s = 2 * (self.width * self.length)
 #       return s


#rectangle1 = Rectangle(10, 5)
#rectangle2 = Rectangle(39, 88)
#rectangle3 = Rectangle(10, 2)
#print(rectangle1.perimeter(), rectangle1.area())
#print(rectangle2.perimeter(), rectangle2.area())
#print(rectangle3.perimeter(), rectangle3.area())

