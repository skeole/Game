import pygame
import math
import random

import sys
sys.path.insert(1, '/Users/shaankeole/Downloads/Coding/Game')

import Graphics.Colors as Colors
import Text_Engine.Version_1.Engine as Text_Engine
import Text_Engine.Version_1.Fonts as Fonts

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

TE = Text_Engine.Text_Engine_V1(gameDisplay)

run = True
pause = False
angle = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pause = not pause
            
    gameDisplay.fill(Colors.green)
    #point_1 = (random.random()*600+100, random.random()*400+100)
    #point_2 = (random.random()*600+100, random.random()*400+100)
    #point_3 = (random.random()*600+100, random.random()*400+100)
    
    #Bezier_Data = Text_Engine.polygons_for_bezier(point_1, point_2, point_3, 5, smoothness=40)
    
    #for i in Bezier_Data:
        #pygame.draw.polygon(gameDisplay, Colors.black, i)
    
    #pygame.draw.polygon(gameDisplay, Colors.gray, Text_Engine.polygon_for_line(point_1, point_2, 5))
    #pygame.draw.polygon(gameDisplay, Colors.gray, Text_Engine.polygon_for_line(point_2, point_3, 5))
    
    #print(pygame.mouse.get_pos())
    TE.type("aaabab", Fonts.bezier, pygame.mouse.get_pos(), 2.0, 2.0, Colors.black, 3, angle=angle, space_between_letters=8, italics=0.5)
    
    pygame.display.update()
    angle += 1
    clock.tick(20)

pygame.quit()