import pygame
import math
import time
import random
import Colors
import Text_Engine.Text_Engine as Text_Engine

import Graphics.Main_Character_V2

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
    TE.type("aa", pygame.mouse.get_pos(), 1, 1, Colors.black, 2, angle=angle, space_between_letters=20, italics=0.1)
    
    pygame.display.update()
    angle += 5
    clock.tick(20)

pygame.quit()