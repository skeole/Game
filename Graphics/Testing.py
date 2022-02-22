import pygame
import math



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


class HumanoidCharacter(object):
    x_vel = 0
    y_vel = 0
    right_arm_angles = [0, 0]
    left_arm_angles = [0, 180]
    right_leg_angles = [-90, 0]
    left_leg_angles = [-90, 0]
    head_color = (128, 128, 128)
    torso_color = (255, 255, 255)
    arm_color = (255, 255, 255)
    leg_color = (255, 255, 255)

    def __init__(self, x, y, height, surface):
        self.x = x
        self.y = y
        self.height = height
        self.right_arm_height = 3*height/4
        self.left_arm_height = 3*height/4
        self.leg_distance_apart = height/16
        self.right_arm_lengths = [height/6, height/5]
        self.left_arm_lengths = [height/6, height/5]
        self.right_leg_lengths = [height/6, 5*height/24]
        self.left_leg_lengths = [height/6, 5*height/24]
        self.head_height = height/6
        self.torso_width = height/8
        self.torso_height = 5*height/12
        self.arm_width = height/72
        self.leg_width = height/54
        self.surface = surface

    def draw(self):
        #torso
        draw_centered_rectangle(self.x, self.y-self.height+self.torso_height/2+self.head_height, self.torso_width, self.torso_height, self.torso_color, surface=self.surface)
        #head
        draw_centered_rectangle(self.x, self.y-self.height+self.head_height/2, self.torso_width, self.head_height, self.head_color, surface=self.surface)
        #arms
        draw_line(self.x+(self.torso_width/2), self.y-self.right_arm_height, self.right_arm_angles[0], self.right_arm_lengths[0], self.arm_color, width=self.arm_width)
        draw_line(self.x+(self.torso_width/2)+self.right_arm_lengths[0]*math.cos(self.right_arm_angles[0]/180.0 * math.pi), self.y-self.right_arm_height-self.right_arm_lengths[0]*math.sin(self.right_arm_angles[0]/180.0 * math.pi), self.right_arm_angles[0]+self.right_arm_angles[1], self.right_arm_lengths[1], self.arm_color, width=self.arm_width)
        draw_line(self.x-(self.torso_width/2), self.y-self.left_arm_height, -self.left_arm_angles[0], -self.left_arm_lengths[0], self.arm_color, width=self.arm_width)
        draw_line(self.x-(self.torso_width/2)-self.left_arm_lengths[0]*math.cos(self.left_arm_angles[0]/180.0 * math.pi), self.y-self.left_arm_height-self.left_arm_lengths[0]*math.sin(self.left_arm_angles[0]/180.0 * math.pi), self.left_arm_angles[0]+self.left_arm_angles[1], self.left_arm_lengths[1], self.arm_color, width=self.arm_width)
        #legs; mid tier
        draw_line(self.x+(self.leg_distance_apart/2), self.y-self.height+self.head_height+self.torso_height, self.right_leg_angles[0], self.right_leg_lengths[0], self.leg_color, width=self.leg_width)
        draw_line(self.x+(self.leg_distance_apart/2)+self.right_leg_lengths[0]*math.cos(self.right_leg_angles[0]/180.0 * math.pi), self.y-self.height+self.head_height+self.torso_height-self.right_leg_lengths[0]*math.sin(self.right_leg_angles[0]/180.0 * math.pi), self.right_leg_angles[0]+self.right_leg_angles[1], self.right_leg_lengths[1], self.leg_color, width=self.leg_width)
        draw_line(self.x-(self.leg_distance_apart/2), self.y-self.height+self.head_height+self.torso_height, -self.left_leg_angles[0], -self.left_leg_lengths[0], self.leg_color, width=self.leg_width)
        draw_line(self.x-(self.leg_distance_apart/2)-self.left_leg_lengths[0]*math.cos(self.left_leg_angles[0]/180.0 * math.pi), self.y-self.height+self.head_height+self.torso_height-self.left_leg_lengths[0]*math.sin(self.left_leg_angles[0]/180.0 * math.pi), self.left_leg_angles[0]+self.left_leg_angles[1], self.left_leg_lengths[1], self.leg_color, width=self.leg_width)

    def get_funky(self):
        self.right_arm_angles[0] += 1
        self.right_arm_angles[1] -= 1
        self.left_arm_angles[0] += 1
        self.left_arm_angles[1] -= 1
        self.right_leg_angles[0] += 1
        self.right_leg_angles[1] -= 1
        self.left_leg_angles[0] += 1
        self.left_leg_angles[1] -= 1

class Sword(object):
    x = None
    y = None
    angle = None
    sword_color = (128, 128, 128)

    def __init__(self, length, width, surface, handle_color=black, handle_type=1):
        self.surface = surface
        self.length = length
        self.width = width
        self.handle_color = handle_color
        self.handle_type = handle_type
        if handle_type == 1:
            self.handle_width = width*0.8
            self.handle_height = (length/3)
            self.handlebar_height = (length/32)
            self.handlebar_width = width*3

    def move(self, new_x, new_y, new_angle):
        self.x = new_x
        self.y = new_y
        self.angle = 0-new_angle*(math.pi/180)

    def draw(self): #setting x, y to MIDDLE of handle

        #rotation:
            #(x, y) rotated theta -> (x*cos(theta) - y*sin(theta), y*cos(theta) + x*sin(theta))

        #handle; 4 vectors - (±height/2, ±width/2)
        pygame.draw.polygon(self.surface, self.handle_color, [(self.x+self.handle_height*math.cos(self.angle)/2-self.handle_width*math.sin(self.angle)/2, self.y+self.handle_width*math.cos(self.angle)/2+self.handle_height*math.sin(self.angle)/2),
                                                              (self.x-self.handle_height*math.cos(self.angle)/2-self.handle_width*math.sin(self.angle)/2, self.y+self.handle_width*math.cos(self.angle)/2-self.handle_height*math.sin(self.angle)/2),
                                                              (self.x-self.handle_height*math.cos(self.angle)/2+self.handle_width*math.sin(self.angle)/2, self.y-self.handle_width*math.cos(self.angle)/2-self.handle_height*math.sin(self.angle)/2),
                                                              (self.x+self.handle_height*math.cos(self.angle)/2+self.handle_width*math.sin(self.angle)/2, self.y-self.handle_width*math.cos(self.angle)/2+self.handle_height*math.sin(self.angle)/2)])

        #now for the actual sword lol; 5 vectors - (handle_height/2+handlebar_height, ±width), (handle_height/2+handlebar_height+length-width/2, ±width),(handle_height/2+handlebar_height+length, 0)
        pygame.draw.polygon(self.surface, self.sword_color, [(self.x+(self.handle_height/2.0+self.handlebar_height)*math.cos(self.angle)-(self.width/2.0)*math.sin(self.angle), self.y+(self.width/2.0)*math.cos(self.angle)+(self.handle_height/2.0+self.handlebar_height)*math.sin(self.angle)),
                                                              (self.x+(self.handle_height/2.0+self.handlebar_height+self.length-self.width/0.8)*math.cos(self.angle)-(self.width/2.0)*math.sin(self.angle), self.y+(self.width/2.0)*math.cos(self.angle)+(self.handle_height/2.0+self.handlebar_height+self.length-self.width/0.8)*math.sin(self.angle)),
                                                              (self.x+(self.handle_height/2.0+self.handlebar_height+self.length)*math.cos(self.angle)-0*math.sin(self.angle), self.y+0*math.cos(self.angle)+(self.handle_height/2.0+self.handlebar_height+self.length)*math.sin(self.angle)),
                                                              (self.x+(self.handle_height/2.0+self.handlebar_height+self.length-self.width/0.8)*math.cos(self.angle)-(0-self.width/2.0)*math.sin(self.angle), self.y+(0-self.width/2.0)*math.cos(self.angle)+(self.handle_height/2.0+self.handlebar_height+self.length-self.width/0.8)*math.sin(self.angle)),
                                                              (self.x+(self.handle_height/2.0+self.handlebar_height)*math.cos(self.angle)-(0-self.width/2.0)*math.sin(self.angle), self.y+(0-self.width/2.0)*math.cos(self.angle)+(self.handle_height/2.0+self.handlebar_height)*math.sin(self.angle))])

        #handle_bar; 4 vectors - (handle_height/2 and handle_height/2+handlebar_height, ±handlebar_width),,
        pygame.draw.polygon(self.surface, self.handle_color, [(self.x+(self.handle_height/2.0)*math.cos(self.angle)-(self.handlebar_width/2.0)*math.sin(self.angle), self.y+(self.handlebar_width/2.0)*math.cos(self.angle)+(self.handle_height/2.0)*math.sin(self.angle)),
                                                              (self.x+(self.handle_height/2.0)*math.cos(self.angle)-(0-self.handlebar_width/2.0)*math.sin(self.angle), self.y+(0-self.handlebar_width/2.0)*math.cos(self.angle)+(self.handle_height/2.0)*math.sin(self.angle)),
                                                              (self.x+(self.handle_height/2.0+self.handlebar_height)*math.cos(self.angle)-(0-self.handlebar_width/2.0)*math.sin(self.angle), self.y+(0-self.handlebar_width/2.0)*math.cos(self.angle)+(self.handle_height/2.0+self.handlebar_height)*math.sin(self.angle)),
                                                              (self.x+(self.handle_height/2.0+self.handlebar_height)*math.cos(self.angle)-(self.handlebar_width/2.0)*math.sin(self.angle), self.y+(self.handlebar_width/2.0)*math.cos(self.angle)+(self.handle_height/2.0+self.handlebar_height)*math.sin(self.angle))])
        #ideas for improvement: make the sword 2 halves, add a line going down the middle, more handle designs


character = HumanoidCharacter(400, 300, 200, gameDisplay)
weapon = Sword(100, 10, gameDisplay)

angle = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    gameDisplay.fill((255, 0, 0))
    weapon.move(475, 150, angle)
    angle += 1
    character.draw()
    weapon.draw()
    pygame.display.update()
    clock.tick(25)

pygame.quit()
