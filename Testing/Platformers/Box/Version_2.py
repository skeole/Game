import sys
sys.path.insert(1, '/Users/shaankeole/Desktop/Coding/Game')

import Graphics.Object_Template as Object_Template

class Box(Object_Template.New_Object):
    def __init__(self, size, ListOfColors, surface):
        self.size = size
        self.ListOfPoints = [[(-size/2, -size/2), 
                              (-size/2, size/2),
                              (size/2, size/2),
                              (size/2, -size/2)]]
        super().__init__(self.ListOfPoints, ListOfColors, surface)
        self.x = 200
        self.y = 0
        self.angle = 0
