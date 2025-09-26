#class Person:

#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def getinfo(self):
#        listinfo = open("hello.txt", "a+")
#        print("Name:", self.name, "Age:", self.age)
#        listinfo.write(f"Name: {self.name}   Age: {self.age}\n")

#tom = Person("Tom", 25)
#n = Person("N", 22)
#tom.getinfo()
#n.getinfo()

import pygame

pygame.init()
resolution = pygame.display.set_mode((720, 480))
pygame.display.update()

resolution_over = False
while not resolution_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            pygame.quit()

    r = pygame.Rect(210, 90, 300, 300)
    r3 = pygame.Rect(390, 175, 100, 100)
    r4 = pygame.Rect(310, 290, 100, 100)
    color = (153, 255, 153)
    color2 = (100, 100, 185)
    color3 = (185, 75, 75)
    pygame.draw.rect(resolution, color, r, 0)
    pygame.draw.rect(resolution, color3, r3, 0)
    pygame.draw.rect(resolution, color3, r4, 0)
    pygame.draw.line(resolution, color, (210, 90), (360, 15))
    pygame.draw.line(resolution, color, (510, 90), (360, 15))
    pygame.display.update()

quit()
