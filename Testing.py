import pygame
import Graphics.Background_V2 as Background
import Object_Collision_V2 as Collision
import math
import time
import random
import Colors
import Object_Collision_V2
import Object_Collision_V1

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

run = True

pause = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pause = not pause
    x1 = random.random()*100
    x2 = random.random()*100
    x3 = random.random()*100
    #x4 = random.random()*100
    y1 = random.random()*100
    y2 = random.random()*100
    y3 = random.random()*100
    #y4 = random.random()*100
    gameDisplay.fill((255, 0, 0))
    pygame.draw.line(gameDisplay, (255, 255, 255), (x1, y1), (x2, y2))
    pygame.draw.circle(gameDisplay, (0, 0, 0), (x3, y3), 5)
    pygame.display.update()
    #a = Object_Collision_V1.intersect(x1, y1, x2, y2, x3, y3, x4, y4)
    #b = Object_Collision_V2.intersect([(x1, y1), (x2, y2)], [(x3, y3), (x4, y4)])
    a = Object_Collision_V1.point_above_line(x3, y3, x1, y1, x2, y2)
    b = Object_Collision_V2.point_above_line((x3, y3), [(x1, y1), (x2, y2)])
    print(a)
    print(b)
    if a != b:
        time.sleep(2)
    print()
    clock.tick(45)

pygame.quit()