import pygame
from os import sys

# Initialize modules of pygame
pygame.init()

# Upload the image


# Create the interface 500x500
window = pygame.display.set_mode((700, 600))
pygame.display.set_caption('Intro Snake Covid')
img = pygame.image.load('Six Pack.png')

# Distance and x, y
x = 50
y = 50
distance_move = 5
condition = True
while condition:
    # speed
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            condition = False

    # Movements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= distance_move
    if keys[pygame.K_RIGHT]:
        x += distance_move
    if keys[pygame.K_UP]:
        y -= distance_move
    if keys[pygame.K_DOWN]:
        y += distance_move
    if keys[pygame.K_ESCAPE]:
        sys.exit(0)

    window.blit(img, (x, y))
    pygame.display.update()

pygame.quit()
