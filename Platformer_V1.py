import pygame
import Values
import math
import Graphics.box as box
import Graphics.Background_V1 as Background

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

box_1 = box.Box(15, Values.black, gameDisplay)
box_1.move(200, 20, 0)

background_1 = Background.Background(gameDisplay)
background_1.update_hitbox()

run = True
pause = False
x_vel = 0.0
y_vel = 0.0
lastTemp = False

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
    box_1.update_hitbox()

    count = 0
    for i in range(15):
        if Values.hitboxes_intersect(box_1.hitbox, background_1.hitbox):
            box_1.y -= 1
            box_1.update_hitbox()
    if count == 15:
        box_1.y += 15
        box_1.angle -= x_vel * r
        box_1.x -= x_vel
        x_vel = 0
        box_1.update_hitbox()

    y_vel += 1
    box_1.y += y_vel
    box_1.update_hitbox()
    if Values.hitboxes_intersect(box_1.hitbox, background_1.hitbox):
        box_1.y -= y_vel
        y_vel = 0
    box_1.y += 1
    box_1.update_hitbox()
    if Values.hitboxes_intersect(box_1.hitbox, background_1.hitbox) and (pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP]):
        y_vel = -15
    box_1.y -= 1
    box_1.update_hitbox()

    gameDisplay.fill(Values.blue)
    box_1.draw()
    background_1.draw()

    pygame.display.update()
    clock.tick(40)

pygame.quit()
