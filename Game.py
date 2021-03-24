# import
import pygame
import random
import time
import sys

pygame.init()

m = 20  # Width and Height

# Create the interface
window = pygame.display.set_mode((735, 475))
pygame.display.set_caption('Snake eats Covid!')

# Add picture
head = pygame.transform.scale(pygame.image.load('Ben.jpg'), (m, m))
tail = pygame.transform.scale(pygame.image.load('Six pack.png'), (m, m))
food = pygame.transform.scale(pygame.image.load('Covid.png'), (m, m))

# Colors
red = pygame.Color(255, 0, 0)
blue = pygame.Color(65, 105, 255)
white = pygame.Color(255, 255, 255)
gray = pygame.Color(128, 128, 128)
black = pygame.Color(0, 0, 0)

# Snake Position
snake_pos = [100, 60]
snake_body = [[100, 60], [80, 60], [60, 60]]
food_x = random.randrange(1, 71)
food_y = random.randrange(1, 45)

if food_x % 2 != 0:
    food_x += 1
if food_y % 2 != 0:
    food_y += 1

food_pos = [food_x * 10, food_y * 10]
food_flat = True

# Direction
direct = 'RIGHT'
change = direct
score = 0


def game_over():
    font = pygame.font.SysFont('consolas', 40)
    surf = font.render('Game Over!', True, red)
    rect = surf.get_rect()
    rect.midtop = (350, 150)
    window.blit(surf, rect)
    show_score(0)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit(0)


def show_score(choice=1):
    font = pygame.font.SysFont('consolas', 20)
    surf = font.render('Score: {0}'.format(score), True, white)
    rect = surf.get_rect()
    if choice == 1:
        rect.midtop = (70, 20)
    else:
        rect.midtop = (360, 230)
    window.blit(surf, rect)


condition = True
while condition:
    # speed
    pygame.time.delay(180)
    for event in pygame.event.get():
        # if the user hit quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        # User interactions
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change = 'RIGHT'
            if event.key == pygame.K_LEFT:
                change = 'LEFT'
            if event.key == pygame.K_UP:
                change = 'UP'
            if event.key == pygame.K_DOWN:
                change = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)

    # User direcitons
    if change == 'RIGHT' and not direct == 'LEFT':
        direct = 'RIGHT'
    if change == 'LEFT' and not direct == 'RIGHT':
        direct = 'LEFT'
    if change == 'UP' and not direct == 'DOWN':
        direct = 'UP'
    if change == 'DOWN' and not direct == 'UP':
        direct = 'DOWN'

    # Update position
    if direct == 'RIGHT':
        snake_pos[0] += m
    if direct == 'LEFT':
        snake_pos[0] -= m
    if direct == 'UP':
        snake_pos[1] -= m
    if direct == 'DOWN':
        snake_pos[1] += m

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_flat = False
    else:
        snake_body.pop()
    # Increase covid
    if food_flat == False:
        food_x = random.randrange(1, 71)
        food_y = random.randrange(1, 45)

        if food_x % 2 != 0:
            food_x += 1
        if food_y % 2 != 0:
            food_y += 1
        food_pos = [food_x * 10, food_y * 10]
    food_flat = True
    # Update the window
    window.fill(black)
    for pos in snake_body:
        window.blit(tail, pygame.Rect(pos[0], pos[1], m, m))
    window.blit(head, pygame.Rect(snake_body[0][0], snake_body[0][1], m, m))
    window.blit(food, pygame.Rect(food_pos[0], food_pos[1], m, m))

    # Snake hit the corner:
    if snake_pos[0] > 710 or snake_pos[0] < 10:
        game_over()
    if snake_pos[1] > 450 or snake_pos[1] < 10:
        game_over()
    # Snake eats itself
    for blood in snake_body[1:]:
        if snake_pos[0] == blood[0] and snake_pos[1] == blood[1]:
            game_over()

    # Frame lines
    pygame.draw.rect(window, gray, (10, 10, 715, 455), 2)
    show_score()
    pygame.display.flip()
