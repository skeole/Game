import pygame
import math

class New_Object(object):
    ListOfPoints = []
    x = None
    y = None
    angle = None
    hitbox = []
    def __init__(self, ListOfPoints, color, surface, width=0): #should be a nested list
                            #ex. [[2, 3, 4, 5], [6, 7, 8, 9]] -> 2 objects with points
                            #2, 3 and 4, 5 for object 1 and 6, 7 and 8, 9 for object 2
        for i in ListOfPoints:
            self.ListOfPoints.append(i)
        self.color = color
        self.surface = surface
        
    def rotateTo(self, angle):
        self.angle = (-1) * angle * math.pi/180.0
    
    def update_hitbox(self):
        self.hitbox = []
        for i in self.ListOfPoints: #for every shape in ListOfPoints
            polygon = []
            for j in range(len(i)/2):
                point = (self.x+(i[2*j]-self.x)*math.cos(self.angle)-(i[2*j+1]-self.y)*math.sin(self.angle), 
                         self.y+(i[2*j]-self.x)*math.sin(self.angle)+(i[2*j+1]-self.y)*math.cos(self.angle))
                polygon.append(point)
            self.hitbox.append(polygon)
    
    def draw(self):
        self.update_hitbox()
        for i in self.hitbox: #for every shape in the hitbox
            pygame.draw.polygon(self.surface, self.color, i, width=self.width)
