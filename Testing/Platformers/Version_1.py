import pygame
import math

import sys
sys.path.insert(1, '/Users/shaankeole/Downloads/Coding/PythonProjects/Pygame/Game')

import Graphics.Colors as Colors
import Collision_Detection.Version_1 as Collision
import Testing.Platformers.Box.Version_1 as Box
import Testing.Platformers.Background.Version_1 as Background

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

box_1 = Box.Box(15, Colors.black, gameDisplay)
box_1.move(200, 20, 0)

background_1 = Background.Background(gameDisplay)
background_1.update_hitbox()

run = True
pause = False
x_vel = 0.0
y_vel = 0.0

r = math.pi / 4.0 / box_1.size

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pause = not pause

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        x_vel += 1
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        x_vel -= 1
    x_vel *= 0.9
    box_1.x += x_vel
    box_1.angle += x_vel * r
    box_1.update_hitbox() #you have to update hitbox whenever you move

    count = 0
    for i in range(15):
        if Collision.hitboxes_intersect(box_1.hitbox, background_1.hitbox):
            count += 1
            box_1.y -= 1
            box_1.update_hitbox()
    if count == 15: #wall basically
        box_1.y += 15
        box_1.angle -= x_vel * r
        box_1.x -= x_vel
        x_vel = 0
        box_1.update_hitbox()
    elif x_vel != 0: #we've gone x, count; math.sqrt(x^2 + count^2)
        if count == 0:
            count = -1
            box_1.y += 1
            for i in range(14):
                if not Collision.hitboxes_intersect(box_1.hitbox, background_1.hitbox):
                    count -= 1
                    box_1.y += 1
                    box_1.update_hitbox()
        if count == -15:
            count = 0
            box_1.y -= 15
            box_1.update_hitbox()
        box_1.x -= x_vel
        box_1.angle -= x_vel * r
        box_1.y += count
        box_1.x += abs(x_vel)/math.sqrt(x_vel*x_vel+count*count) * x_vel
        box_1.angle += abs(x_vel)/math.sqrt(x_vel*x_vel+count*count) * x_vel * r
        box_1.y -= abs(x_vel)/math.sqrt(x_vel*x_vel+count*count) * count
        box_1.update_hitbox()

    y_vel += 1
    box_1.y += y_vel
    box_1.update_hitbox()
    if Collision.hitboxes_intersect(box_1.hitbox, background_1.hitbox):
        box_1.y -= y_vel
        y_vel = 0
    box_1.y += 1
    box_1.update_hitbox()
    if Collision.hitboxes_intersect(box_1.hitbox, background_1.hitbox) and (pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP]):
        y_vel = -15
    box_1.y -= 1
    box_1.update_hitbox()

    gameDisplay.fill(Colors.blue)
    box_1.draw()
    background_1.draw()

    pygame.display.update()
    clock.tick(40)

pygame.quit()
