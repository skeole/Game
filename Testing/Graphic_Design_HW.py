import pygame
import math
import random

import sys
sys.path.insert(1, '/Users/shaankeole/Desktop/Coding/Game')

import Graphics.Colors as Colors
import Text_Engine.Version_1.Engine as Text_Engine
import Text_Engine.Version_1.Fonts as Fonts

pygame.init()

gameDisplay = pygame.display.set_mode((1440, 872))
clock = pygame.time.Clock()

TE = Text_Engine.Text_Engine_V1(gameDisplay)

list_of_crimes = [146, 1019, 3272, 6263, 
                  216, 7960, 13024, 37568]
print(sum(list_of_crimes))
total_number_of_crimes = math.log(sum(list_of_crimes))
print(total_number_of_crimes)

for i in list_of_crimes:
    print(math.log(float(i))/total_number_of_crimes*math.log(float(i))/total_number_of_crimes)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    gameDisplay.fill(Colors.black)
    
    x = 80
    for i in list_of_crimes:
        pygame.draw.polygon(gameDisplay, Colors.gray, [(x, 872), (x+20, 872), (x+20, 100), (x, 100)])
        pygame.draw.polygon(gameDisplay, Colors.white, [(x, 872), (x+20, 872), (x+20, 872-772*math.log(float(i))/total_number_of_crimes*math.log(float(i))/total_number_of_crimes), (x, 872-772*math.log(float(i))/total_number_of_crimes*math.log(float(i))/total_number_of_crimes)])
        x += 180
    
    TE.type("prison bar graph of crimes in phoenix", Fonts.block, (720, 50), 0.5, 0.5, Colors.white, 3, space_between_letters=8)
    
    pygame.display.update()
    clock.tick(20)

pygame.quit()