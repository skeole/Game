#so basically, this is one of those things where you click on the thing
#kinda like btd6 or clash of clans when you place troops, you have to
#click on the unit before placing it

import pygame
import math
import random

import copy
import sys
sys.path.insert(1, '/Users/shaankeole/Downloads/Coding/Game')

import Graphics.Colors as Colors
import Text_Engine.Version_1.Engine as Text_Engine
import Text_Engine.Version_1.Fonts as Fonts
import Graphics.Object_Template as Object_Template

class New_Menu(object):
    list_of_objects = []
    def __init__(self, ListOfPoints, ListOfColors, surface, width, height, backcolor):
        self.ListOfPoints = copy.deepcopy(ListOfPoints)
        self.ListOfColors = copy.deepcopy(ListOfColors)
        self.surface = surface
        self.main = Object_Template.New_Object(ListOfPoints, ListOfColors, surface)
        (self.main).ListOfPoints.insert(0, [
            (float(width)/2.0, float(height)/2.0), 
            (float(width)/2.0, -float(height)/2.0), 
            (-float(width)/2.0, -float(height)/2.0), 
            (-float(width)/2.0, float(height)/2.0)])
        (self.main).ListOfColors.insert(0, backcolor)
    
    def on_clicked(self, x, y):
        (self.list_of_objects).append(Object_Template.New_Object(self.ListOfPoints, self.ListOfColors, self.surface))
        self.move_object(x, y)
    
    def move_object(self, x, y, number=(len(list_of_objects)-1)):
        self.list_of_objects[number].x = x
        self.list_of_objects[number].y = y
    
    def draw(self):
        self.main.draw()
        for object in self.list_of_objects:
            object.draw()