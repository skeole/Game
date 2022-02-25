import pygame
import Graphics.Background_V2 as Background
import Object_Collision_V2 as Collision
import math
import time
import Colors

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

background_1 = Background.Background(Colors.blue, gameDisplay)
background_1.update_hitbox()

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

    gameDisplay.fill(Colors.red)
    
    background_1.draw()
    #pygame.draw.polygon(background_1.surface, background_1.color, background_1.hitbox[0])
    
    pygame.display.update()

    clock.tick(5)

pygame.quit()
