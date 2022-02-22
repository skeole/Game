import pygame
import math
import Sword_V1
import Main_Character_V3

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

black = (0, 0, 0)

def draw_centered_rectangle(x_center, y_center, width, height, color, surface=gameDisplay, fill=0, border_radius=0.0):
    #fill: 0 if fully filled, >1 for line thickness
    pygame.draw.rect(surface, color, [int(x_center - (width/2)), int(y_center - (height/2)), int(width), int(height)], width=int(fill), border_radius=int(border_radius))

def draw_line(x_start, y_start, angle, length, color, surface=gameDisplay, width=1):
    angle_in_radians = angle/180.0 * math.pi
    pygame.draw.circle(surface, color, (int(x_start), int(y_start+1)), int(width/2-1))
    pygame.draw.circle(surface, color, (int(x_start + length*math.cos(angle_in_radians)), int(y_start - length*math.sin(angle_in_radians)+1)), int(width/2-1))
    pygame.draw.circle(surface, color, (int(x_start+2), int(y_start+2)), int(width/2-1))
    pygame.draw.circle(surface, color, (int(x_start + length*math.cos(angle_in_radians))+2, int(y_start - length*math.sin(angle_in_radians)+2)), int(width/2-1))
    pygame.draw.line(surface, color, (int(x_start), int(y_start)), (int(x_start + length*math.cos(angle_in_radians)), int(y_start - length*math.sin(angle_in_radians))), int(width))


character = Main_Character_V3.HumanoidCharacter(400, 300, 200, gameDisplay)
weapon = Sword_V1.Sword(75, 5, gameDisplay)

run = True

weapon.move(475, 150, 0)
angle = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    gameDisplay.fill((255, 0, 0))
    character.draw()
    character.update_hand_and_leg_positions()
    angle += 1
    weapon.move(character.right_hand_x, character.right_hand_y, angle)
    weapon.draw()
    pygame.display.update()
    clock.tick(25)

pygame.quit()
