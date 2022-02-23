import pygame
import Sword_V1
import Main_Character_V3
import box
import math
import time

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

black = (0, 0, 0)

#character = Main_Character_V3.HumanoidCharacter(400, 300, 200, gameDisplay)
#weapon = Sword_V1.Sword(75, 5, gameDisplay)
#weapon2 = Sword_V1.Sword(75, 5, gameDisplay)

box_1 = box.Box(100, black, gameDisplay)
box_1.move(400, 300, 0)

#character_1 = Main_Character_V3.HumanoidCharacter(400, 300, 200, gameDisplay)

x = 400
angle = 0

run = True

pause = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pause = not pause

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        box_1.move(x, 300, angle)
        x += 2.5
        angle -= 1.6875
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        box_1.move(x, 300, angle)
        x -= 2.5
        angle += 1.6875

    gameDisplay.fill((0, 0, 255))
    #character_1.draw()
    box_1.draw()
    pygame.display.update()

    clock.tick(45)

pygame.quit()
