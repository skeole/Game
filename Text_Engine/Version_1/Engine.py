import pygame
import math

import sys
sys.path.insert(1, '/Users/shaankeole/Desktop/Coding/Game')

import Text_Engine.Version_1.Fonts as Fonts
import Graphics.Special_Shapes as Special_Shapes

def translate(point, reference, width, height, italics, angle):
    return (reference[0] + (point[0] + italics * point[1]) * math.cos(angle) * width + point[1] * math.sin(angle) * height, 
            reference[1] - (point[0] + italics * point[1]) * math.sin(angle) * width + point[1] * math.cos(angle) * height)

def letter_hitbox(data, point, weight, width, height, italics=0.0, angle=0, smoothness=3):
    convertedAngle = - angle * math.pi / 180.0
    hitbox = []
    for i in data:
        if i != data[0]: #data[0] = width
            if i[0] == "b": #points go from (a, b) to (width*a/10, height*b/10)
                for j in Special_Shapes.polygons_for_bezier(translate(i[1], point, width, -height, italics, convertedAngle), 
                                             translate(i[2], point, width, -height, italics, convertedAngle), 
                                             translate(i[3], point, width, -height, italics, convertedAngle), 
                                             weight, smoothness=smoothness):
                    hitbox.append(j)
            elif i[0] == "l":
                hitbox.append(Special_Shapes.polygon_for_line(translate(i[1], point, width, -height, italics, convertedAngle), 
                                               translate(i[2], point, width, -height, italics, convertedAngle), 
                                               weight))
    return hitbox

class Text_Engine_V1(object):
    def __init__(self, surface):
        self.surface = surface
    
    def type(self, text, font, point, width, height, color, weight, angle=0, space_between_letters=0, italics=0.0):
        cangle = angle * math.pi/180.0
        temp = -float(space_between_letters)
        word_hitbox = []
        for i in text:
            temp += font[Fonts.CharacterList.index(i)][0] * width
            temp += space_between_letters
        current_distance = -temp/2
        for i in text:
            for j in letter_hitbox(font[Fonts.CharacterList.index(i)], (point[0] + current_distance*math.cos(cangle), point[1] - current_distance*math.sin(cangle)), weight, width, height, italics=italics, angle=-angle):
                word_hitbox.append(j)
            current_distance += font[Fonts.CharacterList.index(i)][0] * width + space_between_letters
        for polygon in word_hitbox:
            pygame.draw.polygon(self.surface, color, polygon)
