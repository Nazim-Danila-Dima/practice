import pygame
import random
import game

RED = (255, 0, 0)

class line:
    def __init__(self):
        self.line_x1 = random.randint(50, 750)
        self.line_x2 = random.randrange(50,750)
        self.line_y1 = random.randint(50,550)
        self.line_y2 = random.randrange(50, 550)
        self.line.fill(RED)

    def draw_line(self):
        draw_line()
        screen.blit(self.line, self.line_x1, self.line_y1, self.line_x2, self.line_y2)
    def calc_line(self, line_x1, line_x2, line_y1, line_y2 ):
        a = float(self.line_y2-self.line_y1)/(self.line_x2-self.line_x1) if self.line_x2 != self.line_x1 else 0
        b = self.line_y1 - a * self.line_x1
        return a, b
    def calc_line_length(self):



