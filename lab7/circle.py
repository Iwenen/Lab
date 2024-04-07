import pygame
import sys

pygame.init()
screen_width, screen_height = 800, 600
screen_fill_color = 'white'
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Circle')
circle_color = 'red'
circle_x = screen_width / 2
circle_y = screen_height / 2
circle_radius = 25
STEP = 20
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_DOWN and circle_y <= screen_height - circle_radius:
        #         circle_y += STEP
        #     if event.key == pygame.K_UP and circle_y >= STEP + circle_radius / 2:
        #         circle_y -= STEP
        #     if event.key == pygame.K_LEFT and circle_x >= STEP + circle_radius / 2:
        #         circle_x -= STEP
        #     if event.key == pygame.K_RIGHT and circle_x <= screen_width - circle_radius:
        #         circle_x += STEP
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and circle_y >= STEP + circle_radius / 4: circle_y -= STEP
    if pressed[pygame.K_DOWN] and circle_y <= screen_height - circle_radius : circle_y += STEP
    if pressed[pygame.K_LEFT] and circle_x >= STEP + circle_radius / 4 : circle_x -= STEP
    if pressed[pygame.K_RIGHT] and circle_x <= screen_width - circle_radius: circle_x += STEP
    screen.fill(screen_fill_color)
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
    pygame.display.flip()
    clock.tick(60)