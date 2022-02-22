import pygame
import Sword_V1
import Main_Character_V3

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

black = (0, 0, 0)

character = Main_Character_V3.HumanoidCharacter(400, 300, 200, gameDisplay)
weapon = Sword_V1.Sword(75, 5, gameDisplay)

run = True

weapon.move(475, 150, 0)
angle = 0
pause = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pause = not pause

    gameDisplay.fill((255, 0, 0))

    if not pause:
        character.get_funky()
        character.update_hand_and_leg_positions()
        angle += 8
        weapon.move(character.right_hand_x, character.right_hand_y, angle)

    character.draw()
    weapon.draw()

    pygame.display.update()

    clock.tick(25)

pygame.quit()
