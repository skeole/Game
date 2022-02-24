black = (0, 0, 0)
white = (234, 234, 234)
gray = (128, 128, 128)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

orange = (255, 128, 0)
yellow = (153, 153, 0)
lime = (76, 153, 0)

def point_above_line(x, y, x1, y1, x2, y2): #definition of "above": y above line, or if vertical, then x value greater
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
        return abs((y2-y1)/(x2-x1) - (y3-y1)/(x3-x1)) < 0.1
    else:
        return (point_above_line(x1, y1, x3, y3, x4, y4) != point_above_line(x2, y2, x3, y3, x4, y4)) and (point_above_line(x3, y3, x1, y1, x2, y2) != point_above_line(x4, y4, x1, y1, x2, y2))

def hitboxes_intersect(hitbox1, hitbox2):
    for i in hitbox1:
        for j in hitbox2:
            if intersect(i[0], i[1], i[2], i[3], j[0], j[1], j[2], j[3]):
                return True
    return False
