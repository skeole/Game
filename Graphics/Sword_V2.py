import Graphics.Object_Template as Object_Template

class Sword(Object_Template.New_Object):
    def __init__(self, length, width, ListOfColors, surface):
        handle_width = width*0.8
        handle_height = (length/3)
        handlebar_height = (length/32)
        handlebar_width = width*3
        
        ListOfPoints = [[(-handle_height/2, -handle_width/2), #handle
                         (-handle_height/2, handle_width/2), 
                         (handle_height/2, handle_width/2), 
                         (handle_height/2, -handle_width/2)], 
                        [(handle_height/2 + handlebar_height, width/2), #sword
                         (handle_height/2 + handlebar_height + length - width, width/2), 
                         (handle_height/2 + handlebar_height + length, 0), 
                         (handle_height/2 + handlebar_height + length - width, -width/2), 
                         (handle_height/2 + handlebar_height, -width/2)], 
                        [(handle_height/2, handlebar_width/2), 
                         (handle_height/2 + handlebar_height, handlebar_width/2), 
                         (handle_height/2 + handlebar_height, -handlebar_width/2), 
                         (handle_height/2, -handlebar_width/2), ]]
        
        super().__init__(ListOfPoints, ListOfColors, surface)
        self.x = 200
        self.y = 0
        self.angle = 0