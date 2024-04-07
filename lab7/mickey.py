import pygame
import sys
from datetime import datetime

pygame.init()

clock = pygame.time.Clock()

window_width, window_height = 1400, 1050
screen = pygame.display.set_mode((window_width, window_height))

bg_image = pygame.image.load('images/mainclock.png')
left_hand = pygame.image.load('images/rightarm.png')
right_hand = pygame.image.load('images/leftarm.png')
rect = bg_image.get_rect(center=(window_width // 2, window_height // 2))

while True:
    screen.blit(bg_image, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    time = datetime.now().time()

    left_angle = -(time.second * 6)
    rotate_left = pygame.transform.rotate(left_hand, left_angle)
    left_rect = rotate_left.get_rect(center = rect.center)
    screen.blit(rotate_left, left_rect.topleft)

    right_angle = -(time.minute * 6)
    rotate_right = pygame.transform.rotate(right_hand, right_angle)
    right_rect = rotate_right.get_rect(center = rect.center)
    screen.blit(rotate_right, right_rect.topleft)
    pygame.display.flip()
    clock.tick(60)

