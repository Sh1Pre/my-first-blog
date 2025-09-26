#class Person:

#   def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def info(self):
#        print(f"Name: {self.name}  Age: {self.age}")


#tom = Person("Tom", 25)
#tom.info()

#from message import *

#print(hello)
#print_message("39!")

#import os


#def get_words(file_name):
#    with open(file_name, encoding = "utf8") as file:
#        text = file.read()
#    text = text.replace("\n", " ")
#    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
#    text = text.lower()
#    words = text .split()
#    words.sort()
#    return words


#def get_words_dict(words):
#    words_dict = dict()
#
 #   for word in words:
 #       if word in words_dict:
 #           words_dict[word] = words_dict[word] + 1
 #       else:
 #           words_dict[word] = 1
 #   return words_dict


#def main():
#    filename = input("Введите путь к файлу: ")
#    if not os.path.exists(filename):
#        print("Указанный файл не существует")
#   else:
#       words = get_words(filename)
#        words_dict = get_words_dict(words)
#        print(f"Кол-во слов: {len(words)}")
#        print(f"Кол-во уникальных слов: {len(words_dict)}")
#        print("Все использованные слова:")
#        for word in words_dict:
#            print(word.ljust(20), words_dict[word])


#if __name__ == "__main__":
#    main()

#import random
#text = open("hello.txt", "a+")
#i = 0

#while i < 100:
#    text.write(str(random.randint(0, 1000)))
#    text.write("\n")
#    i += 1

#n = open("hello.txt", "r+")
#n1 = []
#i = 1
#while i > 100:
#    n2 = n.readline(i)
#    n2.replace("\n", "")
#    n1.append(int(n2))
#    i += 1
#print(n1)

l = []
lines = 1
file = open("hello.txt", "r+")
while lines <= 5:
    a = file.readline()
    if not a:
        break
    print(a)
    a.replace("\n", "")
    l.append(int(a))
    lines += 1

print(l)