import math
import pygame
import random
import numpy as np

FPS = 60
screen_size = (1920, 1080)

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()  # For sound
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Improved Spaceship Game")
clock = pygame.time.Clock()  # For syncing the FPS

# Group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()

# Main surface
main_surface = pygame.Surface(screen_size)
main_surface.fill(BLACK)

# Angle speed etc
angle = 0.0
speed = np.array([0.0, 0.0])
pos = np.array([screen_size[0] / 2, screen_size[1] / 2])

def transform(shape, pos, angle):
    v = -angle + math.pi / 2
    a = np.array(shape)
    t = np.array([[math.cos(v), -math.sin(v)], [math.sin(v), math.cos(v)]])
    r = np.dot(a, t)

    new_shape = []
    for r_point in r:
        newx = r_point[0] + pos[0]
        newy = r_point[1] + pos[1]
        new_shape.append((newx, newy))
    return new_shape

def draw_shape(surface, pos, shape, angle, color=WHITE):
    transformed_shape = transform(shape, pos, angle)
    pygame.draw.aalines(surface, color, True, transformed_shape)

# My shapes
ship = [(-10, -10), (0, 20), (10, -10)]
eng_fire = [(-5, -12), (0, -17), (5, -12)]

# Bullets
bullets = []

def shoot(pos, angle):
    bullet_speed = 10
    bullet_dir = np.array([math.cos(angle), math.sin(angle)])
    bullet_pos = pos + bullet_dir * 20
    bullets.append((bullet_pos, bullet_dir * bullet_speed))

# Game loop
running = True
while running:
    # 1 Process input/events
    clock.tick(FPS)  # Will make the loop run at the same speed all the time
    for event in pygame.event.get():  # Gets all the events which have occurred till now and keeps tab of them.
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not shield:
                shoot(pos, angle)
            if event.key == pygame.K_ESCAPE:
                running = False

    # Get input state
    accelerating = False
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        angle -= 0.1
    if key[pygame.K_d]:
        angle += 0.1
    if key[pygame.K_w]:
        acceleration = np.array([math.cos(angle) * 0.2, math.sin(angle) * 0.2])
        speed += acceleration
        accelerating = True
    shield = key[pygame.K_s]
    
    speed *= 0.99  # Deceleration

    # 2 Update
    pos += speed
    pos[0] %= screen_size[0]
    pos[1] %= screen_size[1]

    for i in range(len(bullets)):
        bullets[i] = (bullets[i][0] + bullets[i][1], bullets[i][1])
        if bullets[i][0][0] < 0 or bullets[i][0][0] > screen_size[0] or bullets[i][0][1] < 0 or bullets[i][0][1] > screen_size[1]:
            bullets[i] = None
    bullets = [b for b in bullets if b is not None]

    # 3 Draw/render
    screen.fill(BLACK)
    main_surface.fill(BLACK)

    if shield:
        pygame.draw.circle(main_surface, CYAN, pos, 30, 2)

    draw_shape(main_surface, pos, ship, angle, WHITE)
    if accelerating:
        draw_shape(main_surface, pos, eng_fire, angle, RED)

    for bullet in bullets:
        pygame.draw.circle(main_surface, GREEN, (int(bullet[0][0]), int(bullet[0][1])), 3)

    screen.blit(main_surface, (0, 0))

    # Done after drawing everything to the screen
    pygame.display.flip()

pygame.quit()
