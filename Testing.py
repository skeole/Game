import pygame
import math
import time
import random
import Colors

import Graphics.Main_Character_V2

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

char = Graphics.Main_Character_V2.Main_Character(gameDisplay, 100)
char.update_hitbox()
print(char.hitbox)

run = True

pause = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pause = not pause
            
    gameDisplay.fill(Colors.green)
    char.draw()
    
    pygame.display.update()
    clock.tick(5)

pygame.quit()