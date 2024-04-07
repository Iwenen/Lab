import pygame
import sys


pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Paint")


shapes = []

drawing = False
start_pos = None
shape = "rectangle"
color = RED

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
            elif event.button == 3:

                for shape_item in shapes:
                    if shape_item[0] == "rectangle":
                        if shape_item[1].collidepoint(event.pos):
                            shapes.remove(shape_item)
                            break
                    elif shape_item[0] == "circle":
                        center = shape_item[1]
                        radius = shape_item[2]
                        if pygame.math.Vector2(event.pos).distance_to(center) <= radius:
                            shapes.remove(shape_item)
                            break
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos
                if shape == "rectangle":
                    rect = pygame.Rect(start_pos[0], start_pos[1],
                                        end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                    shapes.append(("rectangle", rect, color))
                elif shape == "circle":
                    radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])) // 2
                    center = (start_pos[0] + (end_pos[0] - start_pos[0]) // 2,
                              start_pos[1] + (end_pos[1] - start_pos[1]) // 2)
                    shapes.append(("circle", center, radius, color))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shape = "rectangle"
            elif event.key == pygame.K_c:
                shape = "circle"
            elif event.key == pygame.K_e:
                shape = "eraser"
            elif event.key == pygame.K_1:
                color = RED
            elif event.key == pygame.K_2:
                color = GREEN
            elif event.key == pygame.K_3:
                color = BLUE


    screen.fill(WHITE)
    for item in shapes:
        if item[0] == "rectangle":
            pygame.draw.rect(screen, item[2], item[1])
        elif item[0] == "circle":
            pygame.draw.circle(screen, item[3], item[1], item[2])


    if drawing:
        current_pos = pygame.mouse.get_pos()
        if shape == "rectangle":
            rect = pygame.Rect(start_pos[0], start_pos[1],
                                current_pos[0] - start_pos[0], current_pos[1] - start_pos[1])
            pygame.draw.rect(screen, color, rect, 2)
        elif shape == "circle":
            radius = max(abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1])) // 2
            center = (start_pos[0] + (current_pos[0] - start_pos[0]) // 2,
                      start_pos[1] + (current_pos[1] - start_pos[1]) // 2)
            pygame.draw.circle(screen, color, center, radius, 2)
        elif shape == "eraser":
            pygame.draw.rect(screen, WHITE, (current_pos[0], current_pos[1], 20, 20))


    pygame.display.flip()


pygame.quit()
sys.exit()
