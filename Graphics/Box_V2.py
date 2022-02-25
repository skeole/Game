import Graphics.Object_Template as Object_Template

class Box(Object_Template.New_Object):
    def __init__(self, size, color, surface):
        self.size = size
        self.ListOfPoints = [[(-size/2, -size/2), 
                              (-size/2, size/2),
                              (size/2, size/2),
                              (size/2, -size/2)]]
        super().__init__(self.ListOfPoints, color, surface)
        self.x = 200
        self.y = 0
        self.angle = 0