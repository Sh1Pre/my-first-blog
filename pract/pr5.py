#n1 = int(input("Введите первое число: "))
#n2 = int(input("Введите второе число: "))

#if n1 > n2:
#   print("Первое число больше второго")
#elif n1 < n2:
#    print("Первое число меньше второго")
#elif n1 == n2:
#    print("Числа равны")
#else:
#    print("Числа неправильны")

#t = 1
#for t in range(5):
#    surname = input("Введите фамилию: ")

#print(surname)

#n1 = 7
#for n1 in range(n1, 22):
#    print(n1)

#for n in range(0, 50, 2):
#    print(n)

#for n1 in range(50):
#    if n1 % 2 == 0:
#        print(n1)
#    else:
#        continue

#n1 = int(input("Введите число: "))
#
#if n1 % 2 == 0:
#    print("Число четное")
#else:
#    print("Число нечетное")

#class Person:
#
#    def __init__(self, name):
#        self.__name = name

#    @property
#    def name(self):
#        return self.__name

#    def do_nothing(self):
#        print(f"{self.name} does nothing")


#class Employee(Person):

 #   def work(self):
 #       print(f"{self.name} works")


#class Student(Person):
#
 #   def study(self):
#        print(f"{self.name} studies")


#def act(person):
#    if isinstance(person, Student):
#        person.study()
#    elif isinstance(person, Employee):
#        person.work()
#    elif isinstance(person, Person):
#        person.do_nothing()


#tom = Employee("Tom")
#bob = Student("Bob")
#sam = Person("Sam")

#act(tom)
#act(bob)
#act(sam)

#class Person:
#    type = "Person"

#    def __init__(self, name):
#        self.name = name


#tom = Person("Tom")
#bob = Person("Bob")
#print(tom.type)
#print(bob.type)

#Person.type = "Class Person"
#print(tom.type)
#print(bob.type)

#class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def display_info(self):
#        print(self)

#    def __str__(self):
#        return f"Name: {self.name}  Age: {self.age}"


#tom = Person("Tom", 23)
#print(tom)
#tom.display_info()

#class Counter:
#    def __init__(self, value):
#        self.value = value

#    def __add__(self, other):
#        return Counter(self.value + other.value)


#counter1 = Counter(5)
#counter2 = Counter(15)
#counter3 = counter1 + counter2
#print(counter3.value)

#n1 = int(input("Введите первое число: "))
#n2 = int(input("Введите второе число: "))
#n3 = int(input("Введите третье число: "))
#
#if n1 < n2 > n3:
#    print("Второе число максимальное")
#elif n2 < n1 > n3:
#    print("Первое число максимальное")
#else:
#    print("Третье число максимальное")

#class Counter:
#    def __init__(self, value):
#        self.value = value

#    def __bool__(self):
#        return self.value > 0


#def test(counter):
#    if counter:
#        print("Counter = True")
#    else:
#        print("Counter = False")


#counter1 = Counter(3)
#test(counter1)

#counter2 = Counter(-3)
#test(counter2)