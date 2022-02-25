import Graphics.Object_Template as Object_Template

class Background(Object_Template.New_Object):
    def __init__(self, color, surface):
        self.height = surface.get_height()
        self.width = surface.get_width()
        self.ListOfPoints = [[(0, self.height/2), 
                              (self.width/3, self.height/2), 
                              (self.width/2, self.height/4), 
                              (self.width*2/3, self.height/2), 
                              (self.width, self.height/2), 
                              (self.width, self.height), 
                              (0, self.height)]]
        super().__init__(self.ListOfPoints, color, surface)
        self.x = 0
        self.y = self.height
        self.angle = 0

'''
points:

(0, self.height/2)
(self.width/3, self.height/2)
(self.width/2, self.height/4)
(self.width*2/3, self.height/2)
(self.width, self.height/2)
(self.width, self.height)
(0, self.height)
#I might make it so we have to close the thing, but it doesn't really matter :)
'''