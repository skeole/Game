from re import L
import pygame

import sys
sys.path.insert(1, '/Users/shaankeole/Downloads/Coding/Game')

import Collision_Detection.Version_2 as Collision
import Graphics.Colors as Colors
import Graphics.Special_Shapes as Special_Shapes
import Graphics.Object_Template as Object_Template

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

list_of_buttons = []
for i in range(66):
    list_of_buttons.append(Object_Template.New_Object([Special_Shapes.polygon_for_line(
        (0, 0), (0, 0), 15, smoothness=5
    )], [Colors.black], gameDisplay))

for i in range(6):
    for j in range(11):
        list_of_buttons[11*i+j].x = 275+50*i
        list_of_buttons[11*i+j].y = 550-50*j
        list_of_buttons[6*i+j].update_hitbox()

last_button_pressed = -1
list_of_lines = []
letter = []

run = True
pause = False
while run:
    mouse_clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pause = not pause
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
    
    mouse_pos = pygame.mouse.get_pos()
    
    if pygame.key.get_pressed()[pygame.K_p]:
        if letter != []:
            maximum = 0
            for i in letter:
                for j in range(1, len(i)):
                    maximum = max(maximum, i[j][0])

            letter.insert(0, maximum)
            print(str(letter) + ", ")
            letter = []
            last_button_pressed = -1
            list_of_lines = []
            
    gameDisplay.fill(Colors.white)
    for i in range(6):
        x = 275+50*i
        y = 50
        pygame.draw.polygon(gameDisplay, Colors.gray, Special_Shapes.polygon_for_line(
            (x, y), (x, y+500), 4, smoothness=4
        ))
    
    for i in range(11):
        x = 275
        y = 50+50*i
        pygame.draw.polygon(gameDisplay, Colors.gray, Special_Shapes.polygon_for_line(
            (x, y), (x+250, y), 4, smoothness=4
        ))
    
    button_pressed = -1
    
    for i in range(66):
        list_of_buttons[i].draw()
        if mouse_clicked:
            if Collision.point_inside_polygon(mouse_pos, list_of_buttons[i].hitbox[0]):
                button_pressed = i
    
    if button_pressed != -1:
        if last_button_pressed != -1:
            list_of_lines.append(Special_Shapes.polygon_for_line(
                (list_of_buttons[last_button_pressed].x, list_of_buttons[last_button_pressed].y), 
                (list_of_buttons[button_pressed].x, list_of_buttons[button_pressed].y), 4, smoothness=4
            ))
            letter.append(["l", (10 * int(last_button_pressed / 11), 10 * (last_button_pressed % 11)), 
                (10 * int(button_pressed / 11), 10 * (button_pressed % 11))])
            last_button_pressed = -1
        else:
            last_button_pressed = button_pressed
    if last_button_pressed != -1:
        pygame.draw.polygon(gameDisplay, Colors.red, list_of_buttons[last_button_pressed].hitbox[0])
    for i in list_of_lines:
        pygame.draw.polygon(gameDisplay, Colors.red, i)
    
    pygame.display.update()
    clock.tick(20)

pygame.quit()