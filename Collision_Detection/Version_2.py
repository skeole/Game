import math

def point_above_line(point, line): #definition of "above": y above line, or if vertical, then x value greater
    #point format: (x, y)
    #line format: [(x1, y1), (x2, y2)]
    if line[0][0] == line[1][0]:
        return point[0] > line[0][0]
    elif point[0] == line[0][0]:
        return point[1] > line[0][1]
    elif point[0] > line[0][0]:
        return (point[1]-line[0][1])/(point[0]-line[0][0]) > (line[1][1]-line[0][1])/(line[1][0]-line[0][0])
    else:
        return (point[1]-line[0][1])/(point[0]-line[0][0]) < (line[1][1]-line[0][1])/(line[1][0]-line[0][0])

def point_on_line(point, line):
    if abs(line[1][0]-line[0][0]) == 0:
        return abs(line[0][0] - point[0]) < 0.01
    elif abs(point[0]-line[0][0]) == 0:
        return False
    else:
        return (point[1]-line[0][1])/(point[0]-line[0][0]) == (line[1][1]-line[0][1])/(line[1][0]-line[0][0])

def intersect(line_1, line_2):
    if (max(line_1[0][0], line_1[1][0]) < min(line_2[0][0], line_2[1][0])) or (min(line_1[0][0], line_1[1][0]) > max(line_2[0][0], line_2[1][0])) or (max(line_1[0][1], line_1[1][1]) < min(line_2[0][1], line_2[1][1])) or (min(line_1[0][1], line_1[1][1]) > max(line_2[0][1], line_2[1][1])):
        return False #legit zero chance they intersect
    
    temp_1 = line_1[1][0]
    temp_2 = line_2[1][0]
    if line_1[0][0] == line_1[1][0]:
        temp_1 += 0.01
    if line_2[0][0] == line_2[1][0]:
        temp_2 += 0.01
    lein_1 = [line_1[0], (temp_1, line_1[1][1])]
    lein_2 = [line_2[0], (temp_2, line_2[1][1])]
    
    if point_on_line(lein_1[0], lein_2) or point_on_line(lein_1[1], lein_2) or point_on_line(lein_2[0], lein_1) or point_on_line(lein_2[1], lein_1):
        return False #if any of the points are on the line
    else:
        return (point_above_line(lein_1[0], lein_2) != point_above_line(lein_1[1], lein_2)) and (point_above_line(lein_2[0], lein_1) != point_above_line(lein_2[1], lein_1))

def point_inside_polygon(point, polygon, accuracy=6): #we want the inside-ness to be the same for every line
    #solution - very scuffed - kinda LOLLY - but should work
    min_x = 10000000
    min_y = 10000000
    max_x = -10000000
    max_y = -10000000
    for i in polygon:
        min_x = min(min_x, i[0])
        max_x = max(max_x, i[0])
        min_y = min(min_y, i[1])
        max_y = max(max_y, i[1])
    length = math.sqrt((max_x-min_x)*(max_x-min_x)+(max_y-min_y)*(max_y-min_y))
    
    for i in range(accuracy): #go over "accuracy" radial lines
        temp = 0
        
        for j in range(len(polygon)): #add 1 if intersects line, 0.5 for each endpoint it touches
            radial_line = [point, (point[0] + length*math.cos(2*math.pi/accuracy * i), point[1] + length*math.sin(2*math.pi/accuracy * i))]
            if point_on_line(polygon[j], radial_line):
                temp += 1
            if point_on_line(polygon[(j+1) % len(polygon)], radial_line):
                temp += 1
            if intersect(radial_line, 
                         [polygon[j], polygon[(j+1) % len(polygon)]]):
                temp += 2
            #see if the radial line intersects any of the hitbox lines
        
        if temp % 4 != 2:
            return False
    return True

def completely_inside(polygon1, polygon2, accuracy=6):
    for point in polygon1:
        if not point_inside_polygon(point, polygon2, accuracy=accuracy):
            return False
    return True

def shells_intersect(polygon1, polygon2): #only seeing if the outer shells interesect each other
    for i in range(len(polygon1)):
        for j in range(len(polygon2)): #form: (x1, y1)
            if intersect([polygon1[i], polygon1[(i+1) % len(polygon1)]], 
                         [polygon2[j], polygon2[(j+1) % len(polygon2)]]):
                return True
    return False

def polygons_intersect(polygon1, polygon2, accuracy=6):
    return shells_intersect(polygon1, polygon2) or completely_inside(polygon1, polygon2, accuracy=accuracy) or completely_inside(polygon2, polygon1, accuracy=accuracy)

def hitboxes_intersect(hitbox1, hitbox2, accuracy=6):
    for i in hitbox1:
        for j in hitbox2:
            if polygons_intersect(i, j, accuracy=accuracy):
                return True
    return False
