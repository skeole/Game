import Text_Engine.Fonts.Font_1 as Font_1
import math
import pygame

def polygon_for_line(point_1, point_2, width):
    radius = float(width)/2
    if point_1[0] == point_2[0]:
        x = point_1[0]
        y_min = min(point_1[1], point_2[1])
        y_max = max(point_1[1], point_2[1])
        return [(x, y_max+radius), 
                (x+radius/math.sqrt(2), y_max+radius/math.sqrt(2)), 
                (x+radius, y_max), 
                (x+radius, y_min), 
                (x+radius/math.sqrt(2), y_min-radius/math.sqrt(2)), 
                (x, y_min-radius), 
                (x-radius/math.sqrt(2), y_min-radius/math.sqrt(2)), 
                (x-radius, y_min), 
                (x-radius, y_max), 
                (x-radius/math.sqrt(2), y_max+radius/math.sqrt(2)),      
        ]
    else:
        if point_1[0] < point_2[0]:
            x_min = point_1[0]
            y_min = point_1[1]
            x_max = point_2[0]
            y_max = point_2[1]
        else:
            x_max = point_1[0]
            y_max = point_1[1]
            x_min = point_2[0]
            y_min = point_2[1]
        angle = math.atan((y_max-y_min)/(x_max-x_min))
        
        return [(x_max + radius * math.cos(angle + 0 * math.pi/4), y_max + radius * math.sin(angle + 0 * math.pi/4)), 
                (x_max + radius * math.cos(angle + 1 * math.pi/4), y_max + radius * math.sin(angle + 1 * math.pi/4)), 
                (x_max + radius * math.cos(angle + 2 * math.pi/4), y_max + radius * math.sin(angle + 2 * math.pi/4)), 
                (x_min + radius * math.cos(angle + 2 * math.pi/4), y_min + radius * math.sin(angle + 2 * math.pi/4)), 
                (x_min + radius * math.cos(angle + 3 * math.pi/4), y_min + radius * math.sin(angle + 3 * math.pi/4)), 
                (x_min + radius * math.cos(angle + 4 * math.pi/4), y_min + radius * math.sin(angle + 4 * math.pi/4)), 
                (x_min + radius * math.cos(angle + 5 * math.pi/4), y_min + radius * math.sin(angle + 5 * math.pi/4)), 
                (x_min + radius * math.cos(angle + 6 * math.pi/4), y_min + radius * math.sin(angle + 6 * math.pi/4)), 
                (x_max + radius * math.cos(angle + 6 * math.pi/4), y_max + radius * math.sin(angle + 6 * math.pi/4)), 
                (x_max + radius * math.cos(angle + 7 * math.pi/4), y_max + radius * math.sin(angle + 7 * math.pi/4)), 
        ] #yes, there is definitely a way to make this cleaner

def polygons_for_bezier(start_point, mid_point, end_point, width, smoothness=10):
    ListOfPolygons = []
    x_next, y_next = start_point
    i = 0.0
    for j in range(smoothness):
        x_now = x_next
        y_now = y_next
        i += 1.0/smoothness
        x_next = (1-i)*(1-i)*start_point[0] + 2*i*(1-i)*mid_point[0] + i*i*end_point[0]
        y_next = (1-i)*(1-i)*start_point[1] + 2*i*(1-i)*mid_point[1] + i*i*end_point[1]
        ListOfPolygons.append(polygon_for_line((x_now, y_now), (x_next, y_next), width))
    return ListOfPolygons

def translate(point, reference, width, height, italics, angle):
    return (reference[0] + (point[0] + italics * point[1]) * math.cos(angle) * width + point[1] * math.sin(angle) * height, 
            reference[1] - (point[0] + italics * point[1]) * math.sin(angle) * width + point[1] * math.cos(angle) * height)

def letter_hitbox(data, point, weight, width, height, italics=0.0, angle=0, smoothness=3):
    convertedAngle = - angle * math.pi / 180.0
    hitbox = []
    for i in data:
        if i != data[0]: #data[0] = width
            if i[0] == "b": #points go from (a, b) to (width*a/10, height*b/10)
                for j in polygons_for_bezier(translate(i[1], point, width, -height, italics, convertedAngle), 
                                             translate(i[2], point, width, -height, italics, convertedAngle), 
                                             translate(i[3], point, width, -height, italics, convertedAngle), 
                                             weight, smoothness=smoothness):
                    hitbox.append(j)
            elif i[0] == "l":
                hitbox.append(polygon_for_line(translate(i[1], point, width, -height, italics, convertedAngle), 
                                               translate(i[2], point, width, -height, italics, convertedAngle), 
                                               weight))
    return hitbox

class Text_Engine_V1(object):
    font = Font_1.font_1
    def __init__(self, surface):
        self.surface = surface
    
    def type(self, text, point, width, height, color, weight, angle=0, space_between_letters=0, italics=0.0):
        cangle = angle * math.pi/180.0
        temp = -float(space_between_letters)
        word_hitbox = []
        for i in text:
            temp += self.font[Font_1.CharacterList.index(i)][0] * width
            temp += space_between_letters
        current_distance = -temp/2
        for i in text:
            for j in letter_hitbox(self.font[Font_1.CharacterList.index(i)], (point[0] + current_distance*math.cos(cangle), point[1] - current_distance*math.sin(cangle)), weight, width, height, italics=italics, angle=-angle):
                word_hitbox.append(j)
            current_distance += self.font[Font_1.CharacterList.index(i)][0] * width + space_between_letters
        for polygon in word_hitbox:
            pygame.draw.polygon(self.surface, color, polygon)
