import pygame
import Object_Collision_V2 as Collision
import math
import Colors
import Graphics.Box_V2 as Box
import Graphics.Sword_V2 as Sword
import Graphics.Background_V2 as Background
import Graphics.Main_Character_V2 as Main_Character

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

background_color = Colors.white

#box_1 = Box.Box(10, [Colors.black], gameDisplay)
sword_1 = Sword.Sword(25, 2, [Colors.black, Colors.gray, Colors.black], gameDisplay)
box_1 = Main_Character.Main_Character(gameDisplay, 100)

acc = 6
max_count = 5

background_1 = Background.Background([Colors.blue, Colors.orange], gameDisplay)
background_1.update_hitbox()
box_1.update_hitbox()

run = True
pause = False
x_vel = 0.0
y_vel = 0.0
max_vel = 10.0

r = -math.pi #math.pi / 4.0 / box_1.size

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
    if pygame.key.get_pressed()[pygame.K_k]:
        box_1.right_arm_angles[0] += 5
        box_1.update_hitbox()
        count = 0
        for i in range(max_count):
            if Collision.hitboxes_intersect(box_1.hitbox, background_1.hitbox, accuracy=acc):
                count += 1
                box_1.y -= 1
                box_1.update_hitbox()
        if count == max_count:
            box_1.right_arm_angles[0] -= 5
        box_1.y += count
    
    x_vel *= 0.9
    box_1.x += x_vel
    box_1.angle += x_vel * r
    box_1.update_hitbox() #you have to update hitbox whenever you move
    count = 0
    for i in range(max_count):
        if Collision.hitboxes_intersect(box_1.hitbox, background_1.hitbox, accuracy=acc):
            count += 1
            box_1.y -= 1
            box_1.update_hitbox()
    if count == max_count: #wall basically
        box_1.y += max_count
        box_1.angle -= x_vel * r
        box_1.x -= x_vel
        x_vel = 0
        box_1.update_hitbox()
    else: #we've gone x, count; math.sqrt(x^2 + count^2)
        if count == 0:
            count = -1
            box_1.y += 1
            box_1.update_hitbox()
            for i in range(max_count):
                if not Collision.hitboxes_intersect(box_1.hitbox, background_1.hitbox, accuracy=acc):
                    count -= 1
                    box_1.y += 1
                    box_1.update_hitbox()
            count += 1
            box_1.y -= 1
            box_1.update_hitbox()
        if count == -max_count:
            count = 0
            box_1.y -= max_count
            box_1.update_hitbox()
        elif math.sqrt(x_vel*x_vel+count*count) > max_vel:
            box_1.x -= x_vel
            box_1.angle -= x_vel * r
            box_1.y += count
            box_1.x += max_vel/math.sqrt(x_vel*x_vel+count*count) * x_vel
            box_1.angle += max_vel/math.sqrt(x_vel*x_vel+count*count) * x_vel * r
            box_1.y -= max_vel/math.sqrt(x_vel*x_vel+count*count) * count
            box_1.update_hitbox()
    
    y_vel += 1
    box_1.y += y_vel
    box_1.update_hitbox()
    if Collision.hitboxes_intersect(box_1.hitbox, background_1.hitbox, accuracy=acc):
        box_1.y -= y_vel
        y_vel = 0
    box_1.y += 1
    box_1.update_hitbox()
    if Collision.hitboxes_intersect(box_1.hitbox, background_1.hitbox, accuracy=acc) and (pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP]):
        y_vel = -15
    box_1.y -= 1
    box_1.update_hitbox()
    
    (sword_1.x, sword_1.y) = box_1.get_arm_and_leg_positions()
    sword_1.angle = 0

    gameDisplay.fill(background_color)
    box_1.draw()
    background_1.draw()
    sword_1.draw()

    pygame.display.update()
    clock.tick(40)

pygame.quit()
