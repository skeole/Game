import pygame
import math

import sys
sys.path.insert(1, '/Users/shaankeole/Downloads/Coding/Game')

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

class Box(object):
    x = None
    y = None
    angle = None
    hitbox = []

    def __init__(self, size, color, surface):
        self.size = size
        self.color = color
        self.surface = surface

    def move(self, x, y, angle=angle):
        self.x = x
        self.y = y
        self.angle = -angle*math.pi/180

    def update_hitbox(self):
        self.hitbox = []
        self.hitbox.append([self.x+self.size*math.cos(math.pi/4 + self.angle), self.y+self.size*math.sin(math.pi/4 + self.angle), self.x+self.size*math.cos(3*math.pi/4 + self.angle), self.y+self.size*math.sin(3*math.pi/4 + self.angle)])
        self.hitbox.append([self.x+self.size*math.cos(3*math.pi/4 + self.angle), self.y+self.size*math.sin(3*math.pi/4 + self.angle), self.x+self.size*math.cos(5*math.pi/4 + self.angle), self.y+self.size*math.sin(5*math.pi/4 + self.angle)])
        self.hitbox.append([self.x+self.size*math.cos(5*math.pi/4 + self.angle), self.y+self.size*math.sin(5*math.pi/4 + self.angle), self.x+self.size*math.cos(7*math.pi/4 + self.angle), self.y+self.size*math.sin(7*math.pi/4 + self.angle)])
        self.hitbox.append([self.x+self.size*math.cos(7*math.pi/4 + self.angle), self.y+self.size*math.sin(7*math.pi/4 + self.angle), self.x+self.size*math.cos(math.pi/4 + self.angle), self.y+self.size*math.sin(math.pi/4 + self.angle)])

    def draw(self):
        pygame.draw.polygon(self.surface, self.color, [(self.x+self.size*math.cos(math.pi/4 + self.angle), self.y+self.size*math.sin(math.pi/4 + self.angle)),
                                                       (self.x+self.size*math.cos(3*math.pi/4 + self.angle), self.y+self.size*math.sin(3*math.pi/4 + self.angle)),
                                                       (self.x+self.size*math.cos(5*math.pi/4 + self.angle), self.y+self.size*math.sin(5*math.pi/4 + self.angle)),
                                                       (self.x+self.size*math.cos(7*math.pi/4 + self.angle), self.y+self.size*math.sin(7*math.pi/4 + self.angle))])
