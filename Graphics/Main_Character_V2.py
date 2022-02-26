import Graphics.Object_Template as Object_Template
import Colors
import math

class Main_Character(object):

    right_arm_angles = [45, 60]
    left_arm_angles = [45, 60]
    right_leg_angles = [-45, -60]
    left_leg_angles = [-45, -60]
    hitbox = []
    x = 200
    y = 50
    angle = 0

    def __init__(self, surface, height):
        self.height = height
        
        self.arm_lengths = [height/6, height/5]
        self.arm_width = height/72
        
        self.leg_lengths = [height/6, 5*height/24]
        self.leg_width = height/54
        
        self.torso_width = height/8
        self.torso_height = 5*height/12
        
        self.neck_width = height/10
        self.neck_height = height/30
        
        self.head_width = height/8
        self.head_height = height/6
        
        self.torso = Object_Template.New_Object([[(-self.torso_width/2, 0), 
                                                  (self.torso_width/2, 0), 
                                                  (self.torso_width/2, self.torso_height), 
                                                  (-self.torso_width/2, self.torso_height)]], 
                                                [Colors.black], surface)
        self.neck = Object_Template.New_Object([[(-self.neck_width/2, 0), 
                                                  (self.neck_width/2, 0), 
                                                  (self.neck_width/2, self.neck_height), 
                                                  (-self.neck_width/2, self.neck_height)]], 
                                                [Colors.black], surface)
        self.head_and_facial_features = Object_Template.New_Object([
            [(-self.head_width/2, 0), (self.head_width/2, 0), 
             (self.head_width/2, self.head_height), (-self.head_width/2, self.head_height)], 
            [(-self.head_width/4, self.head_height*2/3), (self.head_width/4, self.head_height*2/3), 
             (self.head_width/4, self.head_height*13/20), (-self.head_width/4, self.head_height*12/20)], 
            [(-self.head_width/4, self.head_height/4), (-self.head_width*6/25, self.head_height/4), 
             (-self.head_width*6/25, self.head_height*6/25), (-self.head_width/4, self.head_height*6/25)], 
            [(self.head_width/4, self.head_height/4), (self.head_width*6/25, self.head_height/4), 
             (self.head_width*6/25, self.head_height*6/25), (self.head_width/4, self.head_height*6/25)]], 
                                                [Colors.black, Colors.gray, Colors.gray, Colors.gray], surface)
        self.hair = Object_Template.New_Object([[(-self.head_width/2, 0), 
                                                  (self.head_width/2, 0), 
                                                  (self.head_width/2, self.head_height/10), 
                                                  (-self.head_width/2, self.head_height/10)]], 
                                                [Colors.gray], surface)
        self.right_forearm = Object_Template.New_Object([[(0, -self.arm_width/2), 
                                                          (0, self.arm_width/2), 
                                                          (self.arm_lengths[0], self.arm_width/2), 
                                                          (self.arm_lengths[0], -self.arm_width/2)]], 
                                                        [Colors.black], surface)
        self.left_forearm = Object_Template.New_Object([[(0, -self.arm_width/2), 
                                                          (0, self.arm_width/2), 
                                                          (-self.arm_lengths[0], self.arm_width/2), 
                                                          (-self.arm_lengths[0], -self.arm_width/2)]], 
                                                        [Colors.black], surface)
        self.right_arm = Object_Template.New_Object([[(0, -self.arm_width/2), 
                                                          (0, self.arm_width/2), 
                                                          (self.arm_lengths[1], self.arm_width/2), 
                                                          (self.arm_lengths[1], -self.arm_width/2)]], 
                                                        [Colors.black], surface)
        self.left_arm = Object_Template.New_Object([[(0, -self.arm_width/2), 
                                                          (0, self.arm_width/2), 
                                                          (-self.arm_lengths[1], self.arm_width/2), 
                                                          (-self.arm_lengths[1], -self.arm_width/2)]], 
                                                        [Colors.black], surface)
        self.right_thigh = Object_Template.New_Object([[(0, -self.leg_width/2), 
                                                          (0, self.leg_width/2), 
                                                          (self.leg_lengths[0], self.leg_width/2), 
                                                          (self.leg_lengths[0], -self.leg_width/2)]], 
                                                        [Colors.black], surface)
        self.left_thigh = Object_Template.New_Object([[(0, -self.leg_width/2), 
                                                          (0, self.leg_width/2), 
                                                          (-self.leg_lengths[0], self.leg_width/2), 
                                                          (-self.leg_lengths[0], -self.leg_width/2)]], 
                                                        [Colors.black], surface)
        self.right_calf = Object_Template.New_Object([[(0, -self.leg_width/2), 
                                                          (0, self.leg_width/2), 
                                                          (self.leg_lengths[1], self.leg_width/2), 
                                                          (self.leg_lengths[1], -self.leg_width/2)]], 
                                                        [Colors.black], surface)
        self.left_calf = Object_Template.New_Object([[(0, -self.leg_width/2), 
                                                          (0, self.leg_width/2), 
                                                          (-self.leg_lengths[1], self.leg_width/2), 
                                                          (-self.leg_lengths[1], -self.leg_width/2)]], 
                                                        [Colors.black], surface)
        self.ListOfAppendages = [self.torso, self.neck, self.head_and_facial_features, 
                                 self.hair, self.right_forearm, self.left_forearm, 
                                 self.right_arm, self.left_arm, self.right_thigh, 
                                 self.left_thigh, self.right_calf, self.left_calf]
        self.RelativePointsAndAngles = [[0, 0, 0], [0, -height/30, 0], [0, -height/5, 0], 
                                        [0, -height*13/60, 0], [height/16, 0, 0], [-height/16, 0, 0], 
                                        [height/8, 0, 0], [-height/8, 0, 0], [height/24, 5*height/12, 0], 
                                        [-height/24, 5*height/12, 0], [5*height/12, height/12, 0], [-5*height/12, height/12, 0]]
    
    def update_arms_and_legs(self):
        self.RelativePointsAndAngles[4][2] = self.right_arm_angles[0]
        self.RelativePointsAndAngles[6] = [self.RelativePointsAndAngles[4][0] + self.arm_lengths[0]*math.cos(self.RelativePointsAndAngles[4][2]*math.pi/180.0), 
                                           self.RelativePointsAndAngles[4][1] - self.arm_lengths[0]*math.sin(self.RelativePointsAndAngles[4][2]*math.pi/180.0), 
                                           self.right_arm_angles[1]]
        self.RelativePointsAndAngles[5][2] = -self.left_arm_angles[0]
        self.RelativePointsAndAngles[7] = [self.RelativePointsAndAngles[5][0] - self.arm_lengths[0]*math.cos(self.RelativePointsAndAngles[5][2]*math.pi/180.0), 
                                           self.RelativePointsAndAngles[5][1] + self.arm_lengths[0]*math.sin(self.RelativePointsAndAngles[5][2]*math.pi/180.0), 
                                           -self.left_arm_angles[1]]
        self.RelativePointsAndAngles[8][2] = self.right_leg_angles[0]
        self.RelativePointsAndAngles[10] = [self.RelativePointsAndAngles[8][0] + self.arm_lengths[0]*math.cos(self.RelativePointsAndAngles[8][2]*math.pi/180.0), 
                                           self.RelativePointsAndAngles[8][1] - self.arm_lengths[0]*math.sin(self.RelativePointsAndAngles[8][2]*math.pi/180.0), 
                                           self.right_leg_angles[1]]
        self.RelativePointsAndAngles[9][2] = -self.left_leg_angles[0]
        self.RelativePointsAndAngles[11] = [self.RelativePointsAndAngles[9][0] - self.arm_lengths[0]*math.cos(self.RelativePointsAndAngles[9][2]*math.pi/180.0), 
                                           self.RelativePointsAndAngles[9][1] + self.arm_lengths[0]*math.sin(self.RelativePointsAndAngles[9][2]*math.pi/180.0), 
                                           -self.left_leg_angles[1]]
    
    def align(self, x, y, angle):
        self.update_arms_and_legs()
        ConvertedAngle = -angle*math.pi/180.0
        for i in range(len(self.ListOfAppendages)):
          newAngle = -(angle+self.RelativePointsAndAngles[i][2]) * math.pi/180.0
          self.ListOfAppendages[i].x = x + self.RelativePointsAndAngles[i][0] * math.cos(ConvertedAngle) - self.RelativePointsAndAngles[i][1] * math.sin(ConvertedAngle)
          self.ListOfAppendages[i].y = y + self.RelativePointsAndAngles[i][0] * math.sin(ConvertedAngle) + self.RelativePointsAndAngles[i][1] * math.cos(ConvertedAngle)
          self.ListOfAppendages[i].angle = newAngle
    
    def update_hitbox(self):
        self.align(self.x, self.y, self.angle)  
        self.hitbox = []
        for appendage in self.ListOfAppendages:
            appendage.update_hitbox()
            for polygon in appendage.hitbox:
                self.hitbox.append(polygon)
    
    def draw(self):
        self.align(self.x, self.y, self.angle)
        for appendage in self.ListOfAppendages:
          appendage.draw()
    
    def get_arm_and_leg_positions(self):
        return (self.right_arm.x + self.arm_lengths[1] * math.cos((self.right_arm_angles[1] + self.angle)*math.pi/180.0)*4/5, 
                self.right_arm.y - self.arm_lengths[1] * math.sin((self.right_arm_angles[1] + self.angle)*math.pi/180.0)*4/5)
