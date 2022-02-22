import pygame
import math

def draw_centered_rectangle(x_center, y_center, width, height, color, surface, fill=0, border_radius=0.0):
    #fill: 0 if fully filled, >1 for line thickness
    pygame.draw.rect(surface, color, [int(x_center - (width/2)), int(y_center - (height/2)), int(width), int(height)], width=int(fill), border_radius=int(border_radius))

def draw_line(x_start, y_start, angle, length, color, surface, width=1):
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
        draw_centered_rectangle(self.x, self.y-self.height+self.torso_height/2+self.head_height, self.torso_width, self.torso_height, self.torso_color, self.surface)
        #head
        draw_centered_rectangle(self.x, self.y-self.height+self.head_height/2, self.torso_width, self.head_height, self.head_color, self.surface)
        #arms
        draw_line(self.x+(self.torso_width/2), self.y-self.right_arm_height, self.right_arm_angles[0], self.right_arm_lengths[0], self.arm_color, self.surface, width=self.arm_width)
        draw_line(self.x+(self.torso_width/2)+self.right_arm_lengths[0]*math.cos(self.right_arm_angles[0]/180.0 * math.pi), self.y-self.right_arm_height-self.right_arm_lengths[0]*math.sin(self.right_arm_angles[0]/180.0 * math.pi), self.right_arm_angles[0]+self.right_arm_angles[1], self.right_arm_lengths[1], self.arm_color, self.surface, width=self.arm_width)
        draw_line(self.x-(self.torso_width/2), self.y-self.left_arm_height, -self.left_arm_angles[0], -self.left_arm_lengths[0], self.arm_color, self.surface, width=self.arm_width)
        draw_line(self.x-(self.torso_width/2)-self.left_arm_lengths[0]*math.cos(self.left_arm_angles[0]/180.0 * math.pi), self.y-self.left_arm_height-self.left_arm_lengths[0]*math.sin(self.left_arm_angles[0]/180.0 * math.pi), self.left_arm_angles[0]+self.left_arm_angles[1], self.left_arm_lengths[1], self.arm_color, self.surface, width=self.arm_width)
        #legs; mid tier
        draw_line(self.x+(self.leg_distance_apart/2), self.y-self.height+self.head_height+self.torso_height, self.right_leg_angles[0], self.right_leg_lengths[0], self.leg_color, self.surface, width=self.leg_width)
        draw_line(self.x+(self.leg_distance_apart/2)+self.right_leg_lengths[0]*math.cos(self.right_leg_angles[0]/180.0 * math.pi), self.y-self.height+self.head_height+self.torso_height-self.right_leg_lengths[0]*math.sin(self.right_leg_angles[0]/180.0 * math.pi), self.right_leg_angles[0]+self.right_leg_angles[1], self.right_leg_lengths[1], self.leg_color, self.surface, width=self.leg_width)
        draw_line(self.x-(self.leg_distance_apart/2), self.y-self.height+self.head_height+self.torso_height, -self.left_leg_angles[0], -self.left_leg_lengths[0], self.leg_color, self.surface, width=self.leg_width)
        draw_line(self.x-(self.leg_distance_apart/2)-self.left_leg_lengths[0]*math.cos(self.left_leg_angles[0]/180.0 * math.pi), self.y-self.height+self.head_height+self.torso_height-self.left_leg_lengths[0]*math.sin(self.left_leg_angles[0]/180.0 * math.pi), self.left_leg_angles[0]+self.left_leg_angles[1], self.left_leg_lengths[1], self.leg_color, self.surface, width=self.leg_width)

    def get_funky(self):
        self.right_arm_angles[0] += 1
        self.right_arm_angles[1] -= 1
        self.left_arm_angles[0] += 1
        self.left_arm_angles[1] -= 1
        self.right_leg_angles[0] += 1
        self.right_leg_angles[1] -= 1
        self.left_leg_angles[0] += 1
        self.left_leg_angles[1] -= 1

#ideas for improvement:
#make it so the character doesnt float - legs should always touch ground
#head more round
#legs start above
#perhaps give a function to return hand and leg positions
#add clothes and hair
#MAYBE logos to hair but probably not
