import math


def point_above_line(point, line): #definition of "above": y above line, or if vertical, then x value greater
    #point format: (x, y)
    #line format: [(x1, y1), (x2, y2)]
    if x1 == x2:
        return x > x1
    elif x == x1:
        return False
    elif x > x1:
        return (y-y1)/(x-x1) > (y2-y1)/(x2-x1)
    elif x < x1:
        return (y-y1)/(x-x1) < (y2-y1)/(x2-x1)

def point_on_line(x, y, x1, y1, x2, y2):
    if x1 == x2:
        return x == x1
    else:
        return (y-y1)/(x-x1) == (x2-x1)/(y2-y1)

def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    if (max(x1, x2) < min(x3, x4)) or (min(x1, x2) > max(x3, x4)) or (max(y1, y2) < min(y3, y4)) or (min(y1, y2) > max(y3, y4)):
        return False #legit zero chance they intersect
    if x1 == x2:
        x2 += 0.01
    if x3 == x4:
        x4 += 0.01
    if (y2-y1)/(x2-x1) == (y4-y3)/(x4-x3):
        return abs((y2-y1)/(x2-x1) - (y3-y1)/(x3-x1)) < 0.1 #if theres a bug - make this always return False
    else:
        return (point_above_line(x1, y1, x3, y3, x4, y4) != point_above_line(x2, y2, x3, y3, x4, y4)) and (point_above_line(x3, y3, x1, y1, x2, y2) != point_above_line(x4, y4, x1, y1, x2, y2))

def point_inside_hitbox(x, y, hitbox, accuracy=6): #we want the inside-ness to be the same for every line
    #solution - very scuffed - kinda LOLLY - but should work
    min_x = 10000000
    min_y = 10000000
    max_x = -10000000
    max_y = -10000000
    for i in hitbox:
        min_x = min(min_x, i[0])
        max_x = max(max_x, i[0])
        min_y = min(min_y, i[1])
        max_y = max(max_y, i[1])
    length = math.sqrt((max_x-min_x)*(max_x-min_x)+(max_y-min_y)*(max_y-min_y))
    for i in range(accuracy): #go over "accuracy" radial lines
        temp = 0
        for j in hitbox:
            if intersect(x, y, x+length*math.cos(2*math.pi/accuracy * i), y+length*math.sin(2*math.pi/accuracy * i), j[0], j[1], j[2], j[3]):
                temp += 1
            #see if the radial line intersects any of the hitbox lines
        if temp % 2 == 0:
            return False
    return True

def completely_inside(hitbox1, hitbox2):
    for i in hitbox1:
        if not point_inside_hitbox(i[0], i[1], hitbox2):
            return False
    return True

def shells_intersect(polygon1, polygon2): #only seeing if the outer shells interesect each other
    for i in range(len(polygon1)):
        for j in range(len(polygon2)): #form: (x1, y1)
            if intersect(i[0], i[1], i[2], i[3], j[0], j[1], j[2], j[3]):
                return True
    return False

def polygons_intersect(polygon1, polygon2):
    return shells_intersect(polygon1, polygon2) or completely_inside(polygon1, polygon2) or completely_inside(polygon2, polygon1)

def hitboxes_intersect(hitbox1, hitbox2):
    for i in hitbox1:
        for j in hitbox2:
            if polygons_intersect(i, j):
                return True
    return False
