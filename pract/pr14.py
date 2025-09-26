import pygame
import random

pygame.init()
resolution = pygame.display.set_mode((1000, 850))
i = 0
i2 = 0
i3 = 0
l = []
lines = 1
file = open("hello.txt", "r")

while lines <= 5:
    a = file.readline()
    if not a:
        break
    print(a)
    a.replace("\n", "")
    l.append(int(a))
    lines += 1

pygame.display.update()
font = pygame.font.SysFont("couriernew", 40)

resolution_over = False
while not resolution_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            pygame.quit()

    while i < 7:
        i2 = 0
        while i2 < 7:
            if i2 + (i * 7) in l:
                pygame.draw.rect(resolution, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (0 + (i2 * 150), 0 + (i * 150), 100, 100))
            i2 += 1

        i += 1

    while i3 < 7:
        i2 = 0
        while i2 < 7:
            text = font.render(f"{i2 + (i3 * 7)}", True, (255, 255, 255))
            resolution.blit(text, (50 + (i2 * 150), 50 + (i3 * 150)))
            i2 += 1
        i3 += 1


    pygame.display.update()

quit()