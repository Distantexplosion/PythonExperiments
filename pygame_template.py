import math
import pygame
import random
import numpy as np

FPS = 60
screen_size = (1920, 1070)

# Define some colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("<Your lame game>")
clock = pygame.time.Clock()     ## For syncing the FPS

## group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()

## Main surface
main_surface = pygame.Surface(screen_size)
main_surface.fill(BLACK)

## Angle speed etc
angle = 0.0
speed = (0, 0)
pos = (100, 100)

def transform(shape, pos, angle):
    a = np.array(shape)
    t = np.matrix( ((math.cos(angle), -math.sin(angle)), (math.sin(angle), math.cos(angle))) )
    r = a * t

    new_shape = []

    for r_point in r:
        newx = r_point[0, 0] + pos[0]
        newy = r_point[0, 1] + pos[0]
        new_shape.append((newx, newy))
    return new_shape

def draw_shape(surface, pos, shape, angle, color = WHITE):
    transformed_shape = transform(shape, pos, angle)
    pygame.draw.aalines(surface, color, True, transformed_shape)

## My shapes
ship = [(-10, -10), (0, 20), (10, -10)]
eng_fire = [(-5, -12), (0, -17), (5, -12)]

## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

    ## Get input state
    accelerating = False
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        angle -= .1
    if key[pygame.K_d]:
        angle += .1
    if key[pygame.K_w]:
        speed = (speed[0] + .1, speed[1] + .1)
        accelerating = True
    else:
        speed = (speed[0] * .1, speed[1] * .1)

    # 2 Update
    pos = (pos[0] + speed[0], pos[1] + speed[1])

    # all_sprites.update()

    # 3 Draw/render
    screen.fill(BLACK)
    main_surface.fill(BLACK)

    # aall_sprites.draw(screen)
    ########################

    ### Your code comes here
   
    ## Draw ship
    draw_shape(main_surface, pos, ship, angle, WHITE)
    if(accelerating):
        draw_shape(main_surface, pos, eng_fire, angle, RED)

    screen.blit(main_surface, (0, 0))

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()