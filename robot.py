import pygame
import line
import math
import numpy as np

class robot:
    def __init__(self, x_0, y_0): # на вход нач координаты робота х0 и у0
        self.robot_height = 30 # размеры робота
        self.robot_weigh = 30
        self.speed = 20 # обычная скорость робота, не на линии триггера
        self.max_speed = 50 # скорость робота на триггер линии
        self.rotation_speed = 2 # скорость поворота робота
        self.robot_on = True # включение робота
        self.vector = pygame.math.vector2(1, 1) # вектор move
        self.rect = self.robot.get_rect(x_0, y_0) # получение координат прямоугольника(робота), заданного через draw.rect()
        self.angle = 90 # угол поворота робота
    def get_robot_position(self): # получение позиции робота
        return rect
    def on_robot(self): # метод на включение робота
        self.robot_on = False
    def off_robot(self): # метод на выключение робота
        self.robot_off = True
    def go_line(self, line_x1, line_y1):
        if self.robot_on:
            dx = self.rect - line_x1 # расстояние по оси ОХ до линии
            dy = self.rect - line_y1
            distance = (dx*dx+dy*dy)**0.5 # евклидово расстояние от робота до линии
            if distance > 0:
                vx = dx / distance # синусы и косинусы
                vy = dy / distance
            else:
                distance = 0

            vec = pygame.math.Vector2(vx, vy) # вектор направления и след. нормализуем к 1
            vec.normalize()

            if vec.as_polar() < 0:
                if math.fabs(self.vector.as_polar() - vec.as_polar()) > 2:
                    self.rotation(-1)
                if math.fabs(self.vector.as_polar() - vec.as_polar()) < 2:
                    self.rotation(1)

                if vec2.as_polar() > 0:
                    if math.fabs(self.vector.as_polar() - vec.as_polar()) > 2:
                        self.rotation(1)
                    if math.fabs(self.vector.as_polar() - vec.as_polar()) < 2:
                        self.rotation(-1)
    def move_max_speed(self, line_x_start, line_y_start):
        dx = self.rect - line_x_start  # расстояние по оси ОХ до линии
        dy = self.rect - line_y_start
        distance = (dx * dx + dy * dy) ** 0.5  # евклидово расстояние от робота до линии
        if distance == 0:
            return max_speed
    def turn (self, line_x1, line_y1, x0, y0):    # вычисляем угол поворота робота по отношению к линии старта
        if line_x1 != x0:
            a = float(self.line_y1-self.y0)/(self.line_x1-self.x0)
            b = self.y0 - a * self.x0
            angle_turn = 0
            if a != 0:
                angle_turn = 180 * np.arctan(a) / np.pi
            if a < 0:
                angle_turn = 180 - angle
        return angle_turn














