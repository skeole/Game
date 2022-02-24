import pygame
import Values
import Graphics.box as box
import Graphics.Background as background

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

box_1 = box.Box(50, Values.black, gameDisplay)
box_1.move(400, 200, 0)

background_1 = background.Background(gameDisplay)

run = True
pause = False
x_vel = 0.0
y_vel = 0.0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pause = not pause

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        x_vel += 2
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        x_vel -= 2
    x_vel *= 0.9

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        y_vel -= 2
    y_vel += 1
    y_vel += 0.1

    gameDisplay.fill(Values.red)
    box_1.move(box_1.x+x_vel, box_1.y+y_vel, box_1.angle)
    box_1.draw()
    pygame.display.update()
    clock.tick(25)

pygame.quit()
