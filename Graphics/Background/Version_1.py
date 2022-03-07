import pygame
import math
import Graphics.Colors as Colors

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

class Background(object):
    hitbox = []

    def __init__(self, surface):
        self.level = 1
        self.surface = surface
        self.width = surface.get_width()
        self.height = surface.get_height()

    def set_level(self, level, surface):
        self.level = level

    def draw(self):
        if self.level == 1:
            draw_centered_rectangle(self.width/2, self.height*3/4, self.width, self.height/2, Colors.red, self.surface)
            pygame.draw.polygon(self.surface, Colors.red, [(self.width/3, self.height/2), (self.width/2, self.height/4), (self.width*2/3, self.height/2)])

    def update_hitbox(self):
        self.hitbox = []
        self.hitbox.append([0, self.height/2, self.width/3, self.height/2])
        self.hitbox.append([self.width/3, self.height/2, self.width/2, self.height/4])
        self.hitbox.append([self.width/2, self.height/4, self.width*2/3, self.height/2])
        self.hitbox.append([self.width*2/3, self.height/2, self.width, self.height/2])
        self.hitbox.append([self.width, self.height/2, self.width, self.height])
        self.hitbox.append([self.width, self.height, 0, self.height])
        self.hitbox.append([0, self.height, 0, self.height/2])
