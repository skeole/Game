import pygame
import Sword_V1
import Main_Character_V3
import box
import Background_V1
import math
import time
import Values

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#character_1 = Main_Character_V3.HumanoidCharacter(400, 300, 200, gameDisplay)
#weapon = Sword_V1.Sword(75, 5, gameDisplay)
#weapon2 = Sword_V1.Sword(75, 5, gameDisplay)

box_1 = box.Box(50, Values.black, gameDisplay)
box_1.move(400, 500, 0)

background_1 = Background.Background(gameDisplay)

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
        box_1.move(x, box_1.y, angle)
        x += 2.5
        angle -= 4
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        box_1.move(x, box_1.y, angle)
        x -= 2.5
        angle += 4

    box_1.update_hitbox()
    background_1.update_hitbox()

    if Values.hitboxes_intersect(box_1.hitbox, background_1.hitbox):
        box_1.y -= 5
    else:
        box_1.y += 1

    gameDisplay.fill((0, 0, 255))
    background_1.draw()
    #character_1.draw()
    #character_1.get_funky()
    box_1.draw()
    pygame.display.update()

    clock.tick(25)

pygame.quit()
