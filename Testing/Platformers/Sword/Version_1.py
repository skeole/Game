import pygame
import math

import sys
sys.path.insert(1, '/Users/shaankeole/Downloads/Coding/Game')

black = (0, 0, 0)

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

#pygame.draw.polygon(gameDisplay, black, [(x1, y1), (x2, y2), ...], width=0)

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
