import os.path
import pygame
import random
import pyautogui
import robot
import line
import sub
from os import path


# Цвета и параметры
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 1920
HEIGHT = 1080

# Юзаем pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("SIM ROBOT")





# окно
def draw_win():
    screen.fill(WHITE)
    pygame.draw.rect(screen, (171, 156, 169), (0, 0, WIDTH, HEIGHT))
    pygame.draw.circle(screen, BLACK, (40, 50), 20, 0) # робот на начальных координатах
    pygame.draw.line(screen, RED, (144, 350), (737, 740), 11) # координаты линии



# цикл приложения
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw_win()
    pygame.display.flip()
    # включение робота посредством запросов
    if str(sub.on_message()) == "start engine":
        robot.on_robot()
    if str(sub.on_message()) == "stop engine":
        robot.off_robot()
    if (robot.x0 != robot.line_x1) and (robot.y0 != robot.line_y1):
       robot.go_line(robot.line_x1, robot.line_y1) # если координаты робота и линии неравны, то робот движется к нач. координатам линии
       if (robot.x0 == robot.line_x1) and (robot.y0 == robot.line_y1): # если координаты робота стали равны, то робот едет с макс. скоростью к конечным координатам линии
           robot.move_max_speed(line_x1, line_y1, line_x2, line_y2)



pygame.image.save(screen, os.path.join('OpenCV','1.jpg'))
pygame.quit()
quit()