import pygame
import math
import random

import sys
sys.path.insert(1, '/Users/shaankeole/Downloads/Coding/Game')

#import Graphics.Colors as Colors

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

run = True
pause = False
mouse_clicked = False
mouse_released = False
mouse_down = False
last_mouse_position = (0, 0)
mouse_position = (0, 0)
mouse_change = (0, 0)

background_color = (0, 0, 0)

while run:
    
    last_mouse_position = mouse_position
    mouse_position = pygame.mouse.get_pos()
    mouse_change[0] = mouse_position[0] - last_mouse_position[0]
    mouse_change[1] = mouse_position[1] - last_mouse_position[1]
    
    mouse_clicked = False
    mouse_released = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
            mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_released = True
            mouse_down = False
    
    if pygame.key.get_pressed()[pygame.K_p]:
        pause = not pause
    
    gameDisplay.fill(background_color.green)
    
    pygame.display.update()
    clock.tick(20)

pygame.quit()