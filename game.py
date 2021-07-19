import pygame
import random
from os import path

# Цвета и параметры
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 800
HEIGHT = 600

# Юзаем pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SIM ROBOT")


# окно
def draw_win():
    screen.fill(WHITE)
    pygame.draw.rect(screen, (171, 156, 169), (0, 0, WIDTH, HEIGHT))
    pygame.draw.circle(screen, BLACK, (70, 80), 20, 0)
    pygame.draw.line(screen, RED, (170, 240), (480, 530), 11)


# цикл приложения
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # включение робота через enter
                robot.on_robot()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:  # выключяение робота через backspace
                robot.off_robot()

    draw_win()
    pygame.display.flip()

pygame.quit()
quit()