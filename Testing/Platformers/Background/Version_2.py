import sys
sys.path.insert(1, '/Users/shaankeole/Desktop/Coding/Game')

import Graphics.Object_Template as Object_Template

class Background(Object_Template.New_Object):
    def __init__(self, ListOfColors, surface):
        self.window_height = surface.get_height()
        self.window_width = surface.get_width()
        self.ListOfPoints = [[(0, self.window_height/2), 
                              (self.window_width/3, self.window_height/2), 
                              (self.window_width/2, self.window_height/4), 
                              (self.window_width*2/3, self.window_height/2), 
                              (self.window_width, self.window_height/2), 
                              (self.window_width, self.window_height), 
                              (0, self.window_height)], 
                             [(self.window_width*3/4, self.window_height*2/5), 
                              (self.window_width, self.window_height*2/5), 
                              (self.window_width, self.window_height/3), 
                              (self.window_width*3/4, self.window_height/3)]]
        super().__init__(self.ListOfPoints, ListOfColors, surface)
        
        self.x = 0
        self.y = 0
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