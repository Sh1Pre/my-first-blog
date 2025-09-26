import pygame

pygame.init()
resolution = pygame.display.set_mode((1000, 800))
font = pygame.font.SysFont("couriernew", 40)
text = font.render("Снеговик", True, (255, 255, 255))
resolution.blit(text, (50, 50))
pygame.display.update()

resolution_over = False
while not resolution_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            pygame.quit()

    colorW = (255, 255, 255)
    colorB = (80, 40, 50)
    color0 = (0, 0, 0)
    colorG = (0, 191, 255)
    colorR = (255, 0, 0)
    colorY = (255, 255, 0)
    colorZ = (0, 255, 0)

    pygame.draw.circle(resolution, colorW, (500, 650), 150)
    pygame.draw.circle(resolution, colorW, (500, 450), 125)
    pygame.draw.circle(resolution, colorW, (500, 275), 100)

    pygame.draw.line(resolution, colorB, (375, 450), (200, 400), 5)
    pygame.draw.line(resolution, colorB, (625, 450), (800, 400), 5)

    pygame.draw.circle(resolution, color0, (450, 250), 20)
    pygame.draw.circle(resolution, color0, (550, 250), 20)

    pygame.draw.rect(resolution, colorW, (600, 20, 910, 200))
    pygame.draw.circle(resolution, colorG, (700, 100), 40, 5)
    pygame.draw.circle(resolution, color0, (790, 100), 40, 5)
    pygame.draw.circle(resolution, colorR, (880, 100), 40, 5)
    pygame.draw.circle(resolution, colorY, (745, 130), 40, 5)
    pygame.draw.circle(resolution, colorZ, (835, 130), 40, 5)

    pygame.display.update()

quit()