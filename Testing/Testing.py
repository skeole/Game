import pygame
import math
import random

import sys
sys.path.insert(1, '/Users/shaankeole/Downloads/Coding/PythonProjects/Pygame/Game')

import Graphics.Colors as Colors
import Text_Engine.Version_1.Engine as Text_Engine
import Text_Engine.Version_1.Fonts as Fonts
import Menu.Drop_And_Place as Drop_And_Place
import Collision_Detection.Version_2 as Collision_Detection

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

TE = Text_Engine.Text_Engine_V1(gameDisplay)
c = Drop_And_Place.New_Menu([[(-10, 0), (0, 10), (10, 0), (0, -10)]], [Colors.black], gameDisplay, 40, 40, Colors.red)
c.main.x = 400
c.main.y = 300
c.main.update_hitbox()
run = True
pause = False
angle = 0
mouse_clicked = False
mouse_down = False
mouse = (0, 0)
last_clicked = False
while run:
    mouse = pygame.mouse.get_pos()
    mouse_clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pause = not pause
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
            mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
            last_clicked = False
    
    gameDisplay.fill(Colors.green)
    
    if mouse_down:
        TE.type("01234567890,.()", Fonts.numbers, (120, 50), 0.33, 0.30, Colors.black, 1, space_between_letters=3)
    
    if mouse_clicked and Collision_Detection.point_inside_polygon(mouse, c.main.hitbox[0]):
        c.on_clicked(mouse[0], mouse[1])
        last_clicked = True
    
    if mouse_down and last_clicked:
        c.move_object(mouse[0], mouse[1])
    
    c.draw()
    pygame.display.update()
    clock.tick(20)

pygame.quit()