import pygame
# import line
import math
import numpy as np

import sub_cv
import sub_hmi


class robot:
    def __init__(self, x0, y0):  # на вход нач координаты робота х0 и у0
        self.robot_height = 30  # размеры робота
        self.robot_weigh = 30
        self.speed = 20  # обычная скорость робота, не на линии триггера
        self.max_speed = 50  # скорость робота на триггер линии
        self.rotation_speed = 2  # скорость поворота робота
        self.robot_on = True  # включение робота
        self.vector = pygame.math.vector2(1, 1)  # вектор move
        self.x0 = x0  # координаты начала(робота)
        self.y0 = y0
        self.angle = 90  # угол поворота робота

    def on_robot(self):  # метод на включение робота
        self.robot_on = False
        print("on")

    def off_robot(self):  # метод на выключение робота
        self.robot_off = True
        print("off")

    def go_line(self, left_x, left_y, x0, y0):
        if self.robot_on:
            dx = left_x - x0  # расстояние по оси ОХ до линии
            dy = left_y - y0
            distance = (dx * dx + dy * dy) ** 0.5  # евклидово расстояние от робота до линии
            if distance > 0:
                vx = dx / distance  # синусы и косинусы
                vy = dy / distance
            # else:
            # return max_speed()

            vec = pygame.math.Vector2(vx, vy)  # вектор направления и след. нормализуем к 1
            vec.normalize()

            if vec.as_polar() < 0:
                if math.fabs(self.vector.as_polar() - vec.as_polar()) > 2:
                    self.rotation(-1)
                if math.fabs(self.vector.as_polar() - vec.as_polar()) < 2:
                    self.rotation(1)

                if vec.as_polar() > 0:
                    if math.fabs(self.vector.as_polar() - vec.as_polar()) > 2:
                        self.rotation(1)
                    if math.fabs(self.vector.as_polar() - vec.as_polar()) < 2:
                        self.rotation(-1)

    def move_max_speed(self, line_x_start, line_y_start, line_x2, line_y2):
        self.turn(line_x2, line_y2, line_x_start, line_y_start)
        dx = line_x2 - line_x_start  # расстояние по оси ОХ до линии
        dy = line_y2 - line_y_start
        distance = (dx * dx + dy * dy) ** 0.5  # евклидово расстояние от начала линии до конца
        # if distance > 0:
        # return max_speed()

    def turn(self, line_x1, line_y1, x0, y0):  # вычисляем угол поворота робота по отношению к линии старта
        if line_x1 != x0:
            a = float(self.line_y1 - self.y0) / (self.line_x1 - self.x0)
            b = self.y0 - a * self.x0
            angle_turn = 0
            if a != 0:
                angle_turn = 180 * np.arctan(a) / np.pi
            if a < 0:
                angle_turn = 180 - angle_turn
        return angle_turn


#sub_hmi.run()
#if sub_hmi.mess == "start engine":
    #robot.on_robot()
#elif sub_hmi.mess == "stop engine":
    #robot.off_robot()
sub_cv.run()
coor = sub_cv.mess.split(" ")
left_x = int(coor[0])
left_y = int(coor[1])
right_x = int(coor[2])
right_y = int(coor[3])
print(left_x)
print(left_y)
print(right_x)
print(right_y)

