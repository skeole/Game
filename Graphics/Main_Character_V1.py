import pygame
import math
import time

pygame.init()
clock = pygame.time.Clock()

display_width = 800.0
display_height = display_width*3/4

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Main Character")

black = (0, 0, 0)
white = (234, 234, 234)
gray = (128, 128, 128)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

orange = (255, 128, 0)
yellow = (153, 153, 0)
lime = (76, 153, 0)

char_x = 400
char_y = 300
torso_width = 60
torso_height = 150
arm_height = 10
right_arm_angle = 30
right_elbow_angle = 30
right_arm_lengths = [30, 45]
left_arm_angle = -60
left_elbow_angle = -30
left_arm_lengths = [30, 45]
head_center = 50
leg_distance_apart = 40
right_leg_angle = -60
right_knee_angle = -30
right_leg_lengths = [30, 45]
left_leg_lengths = [30, 45]
left_leg_angle = -60
left_knee_angle = -30

#will try to make all of these a function based on "height" in V2, then you can choose specific parts

#pixAr = pygame.PixelArray(gameDisplay)
#pixAr[10][20] = (0, 0, 0) - in theory you could assign each pixel a value

def draw_centered_rectangle(x_center, y_center, width, height, color, surface=gameDisplay, fill=0, border_radius=0.0):
    #fill: 0 if fully filled, >1 for line thickness
    pygame.draw.rect(surface, color, [int(x_center - (width/2)), int(y_center - (height/2)), int(width), int(height)], width=int(fill), border_radius=int(border_radius))

def draw_line(x_start, y_start, angle, length, color, surface=gameDisplay, width=1):
    angle_in_radians = angle/180.0 * math.pi
    pygame.draw.circle(surface, color, (int(x_start), int(y_start+1)), width/2-1)
    pygame.draw.circle(surface, color, (int(x_start + length*math.cos(angle_in_radians)), int(y_start - length*math.sin(angle_in_radians)+1)), width/2-1)
    pygame.draw.circle(surface, color, (int(x_start+2), int(y_start+2)), width/2-1)
    pygame.draw.circle(surface, color, (int(x_start + length*math.cos(angle_in_radians))+2, int(y_start - length*math.sin(angle_in_radians)+2)), width/2-1)
    pygame.draw.line(surface, color, (int(x_start), int(y_start)), (int(x_start + length*math.cos(angle_in_radians)), int(y_start - length*math.sin(angle_in_radians))), width)


run = True
#print(math.cos(math.pi)) it uses radians
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    print(clock.get_time())
    gameDisplay.fill(white)

    #torso
    draw_centered_rectangle(char_x, char_y, torso_width, torso_height, black)

    #arms
    draw_line(char_x+(torso_width/2), char_y-arm_height, right_arm_angle, right_arm_lengths[0], black, width=10)
    draw_line(char_x+(torso_width/2)+right_arm_lengths[0]*math.cos(right_arm_angle/180.0 * math.pi), char_y-arm_height-right_arm_lengths[0]*math.sin(right_arm_angle/180.0 * math.pi), right_elbow_angle+right_arm_angle, right_arm_lengths[1], black, width=10)
    draw_line(char_x-(torso_width/2), char_y-arm_height, -left_arm_angle, -left_arm_lengths[0], black, width=10)
    draw_line(char_x-(torso_width/2)-left_arm_lengths[0]*math.cos(left_arm_angle/180.0 * math.pi), char_y-arm_height-left_arm_lengths[0]*math.sin(left_arm_angle/180.0 * math.pi), left_elbow_angle+left_arm_angle, left_arm_lengths[1], black, width=10)

    #head
    draw_centered_rectangle(char_x, char_y-head_center, torso_width, torso_height-head_center*2, yellow)

    #legs
    draw_line(char_x+(leg_distance_apart/2), char_y+torso_height/2, right_leg_angle, right_leg_lengths[0], black, width=10)
    draw_line(char_x+(leg_distance_apart/2)+right_leg_lengths[0]*math.cos(right_leg_angle/180.0 * math.pi), char_y+torso_height/2-right_leg_lengths[0]*math.sin(right_leg_angle/180.0 * math.pi), right_leg_angle+right_knee_angle, right_leg_lengths[1], black, width=10)
    draw_line(char_x-(leg_distance_apart/2), char_y+torso_height/2, -left_leg_angle, -left_leg_lengths[0], black, width=10)
    draw_line(char_x-(leg_distance_apart/2)-left_leg_lengths[0]*math.cos(left_leg_angle/180.0 * math.pi), char_y+torso_height/2-left_leg_lengths[0]*math.sin(left_leg_angle/180.0 * math.pi), left_leg_angle+left_knee_angle, left_leg_lengths[1], black, width=10)

    pygame.display.update()
    clock.tick(10)

pygame.quit()
