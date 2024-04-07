import sys

import pygame
from random import randrange

RES = 800
SIZE = 50


x, y = randrange(0,RES,SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
snake = [(x,y)]
dx, dy = 0, 0
fps = 5
score = 0
level = 0

pygame.init()
sc = pygame.display.set_mode((RES,RES))
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_level = pygame.font.SysFont('Arial', 26, bold=True)

while True:
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc, 'green',(i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(sc, 'red', (*apple, SIZE, SIZE))

    render_score = font_score.render(f'SCORE: {score}', 1, 'orange')
    sc.blit(render_score, (5, 5))
    render_level = font_score.render(f'LEVEL: {level}', 1, 'orange')
    sc.blit(render_level, (5, 30))
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1
        if score % 3 == 0:
            fps += 3

    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', True, 'orange')
            sc.blit(render_end, (RES // 2 - 200, RES // 2 - 100))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}