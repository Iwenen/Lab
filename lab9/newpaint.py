import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создание окна
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Рисование фигур")

# Список для хранения нарисованных фигур
shapes = []

# Переменные для рисования
drawing = False
start_pos = None
shape = "rectangle"  # Изначально выбрано рисование прямоугольников
color = RED  # Изначальный цвет

# Основной цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                drawing = True
                start_pos = event.pos
            elif event.button == 3:  # Правая кнопка мыши
                # Удаление фигуры, на которую нажали мышью
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
            if event.button == 1:  # Левая кнопка мыши
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
                elif shape == "square":
                    side_length = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    square_rect = pygame.Rect(start_pos[0], start_pos[1], side_length, side_length)
                    shapes.append(("square", square_rect, color))
                elif shape == "right_triangle":
                    a = end_pos[0] - start_pos[0]
                    b = end_pos[1] - start_pos[1]
                    hypotenuse = math.sqrt(a**2 + b**2)
                    right_triangle_points = [(start_pos[0], start_pos[1]), (end_pos[0], start_pos[1]), end_pos]
                    shapes.append(("right_triangle", right_triangle_points, color))
                elif shape == "equilateral_triangle":
                    side_length = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    equilateral_triangle_height = side_length * math.sqrt(3) / 2
                    equilateral_triangle_points = [(start_pos[0], end_pos[1]),
                                                   ((start_pos[0] + end_pos[0]) // 2, start_pos[1]),
                                                   (end_pos[0], end_pos[1])]
                    shapes.append(("equilateral_triangle", equilateral_triangle_points, color))
                elif shape == "rhombus":
                    rhombus_width = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    rhombus_height = rhombus_width
                    rhombus_points = [((start_pos[0] + end_pos[0]) // 2, start_pos[1]),
                                      (end_pos[0], (start_pos[1] + end_pos[1]) // 2),
                                      ((start_pos[0] + end_pos[0]) // 2, end_pos[1]),
                                      (start_pos[0], (start_pos[1] + end_pos[1]) // 2)]
                    shapes.append(("rhombus", rhombus_points, color))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Нажатие клавиши "r" для выбора рисования прямоугольников
                shape = "rectangle"
            elif event.key == pygame.K_c:  # Нажатие клавиши "c" для выбора рисования кругов
                shape = "circle"
            elif event.key == pygame.K_s:  # Нажатие клавиши "s" для выбора рисования квадрата
                shape = "square"
            elif event.key == pygame.K_t:  # Нажатие клавиши "t" для выбора рисования прямоугольного треугольника
                shape = "right_triangle"
            elif event.key == pygame.K_e:  # Нажатие клавиши "e" для выбора рисования равностороннего треугольника
                shape = "equilateral_triangle"
            elif event.key == pygame.K_h:  # Нажатие клавиши "h" для выбора рисования ромба
                shape = "rhombus"
            elif event.key == pygame.K_1:  # Нажатие клавиши "1" для выбора красного цвета
                color = RED
            elif event.key == pygame.K_2:  # Нажатие клавиши "2" для выбора зеленого цвета
                color = GREEN
            elif event.key == pygame.K_3:  # Нажатие клавиши "3" для выбора синего цвета
                color = BLUE

    # Рисование фигур
    screen.fill(WHITE)
    for item in shapes:
        if item[0] == "rectangle":
            pygame.draw.rect(screen, item[2], item[1])
        elif item[0] == "circle":
            pygame.draw.circle(screen, item[3], item[1], item[2])
        elif item[0] == "square":
            pygame.draw.rect(screen, item[2], item[1])
        elif item[0] == "right_triangle":
            pygame.draw.polygon(screen, item[2], item[1])
        elif item[0] == "equilateral_triangle":
            pygame.draw.polygon(screen, item[3], item[1])
        elif item[0] == "rhombus":
            pygame.draw.polygon(screen, item[3], item[1])

    # Рисование текущей фигуры в реальном времени при удерживании кнопки мыши
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
        elif shape == "square":
            side_length = max(abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
            square_rect = pygame.Rect(start_pos[0], start_pos[1], side_length, side_length)
            pygame.draw.rect(screen, color, square_rect, 2)
        elif shape == "right_triangle":
            a = current_pos[0] - start_pos[0]
            b = current_pos[1] - start_pos[1]
            hypotenuse = math.sqrt(a**2 + b**2)
            right_triangle_points = [(start_pos[0], start_pos[1]), (current_pos[0], start_pos[1]), current_pos]
            pygame.draw.polygon(screen, color, right_triangle_points, 2)
        elif shape == "equilateral_triangle":
            side_length = max(abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
            equilateral_triangle_height = side_length * math.sqrt(3) / 2
            equilateral_triangle_points = [(start_pos[0], current_pos[1]),
                                           ((start_pos[0] + current_pos[0]) // 2, start_pos[1]),
                                           (current_pos[0], current_pos[1])]
            pygame.draw.polygon(screen, color, equilateral_triangle_points, 2)
        elif shape == "rhombus":
            rhombus_width = max(abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
            rhombus_height = rhombus_width
            rhombus_points = [((start_pos[0] + current_pos[0]) // 2, start_pos[1]),
                              (current_pos[0], (start_pos[1] + current_pos[1]) // 2),
                              ((start_pos[0] + current_pos[0]) // 2, current_pos[1]),
                              (start_pos[0], (start_pos[1] + current_pos[1]) // 2)]
            pygame.draw.polygon(screen, color, rhombus_points, 2)

    # Обновление экрана
    pygame.display.flip()

# Выход из программы
pygame.quit()
sys.exit()
