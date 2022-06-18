# class player
import pygame
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
y_temp = 0
x_temp = 0
dir = 0
from gl import *

class player:
    def __init__(self,rect_x_end,rect_y_end,color,x,y):
        self.x = x
        self.y = y
        self.color = color # Цвет
        self.rect_x_end = rect_x_end # размер (h_w_rect)
        self.rect_y_end = rect_y_end # размер (h_w_rect)
        self.x_map = int(self.x / self.rect_x_end) # корды карты
        self.y_map = int(self.y / self.rect_y_end) # корды карты
        self.old_x = 0# x для востановления
        self.old_y = 0# y для востановления
        self.dir = 0
    def move(self,dir,map=map): # перемещятся (UP,DOWN,LEFT,RIGHT)
        self.dir = dir
        self.old_x = self.x
        self.old_y = self.y
        if dir == 'UP':
            self.y -= self.rect_y_end
        elif dir == 'DOWN':
            self.y += self.rect_y_end
        elif dir == 'LEFT':
            self.x -= self.rect_x_end
        elif dir == 'RIGHT':
            self.x += self.rect_x_end
        else:
            exit(NameError)
        self.x_map = int(self.x / self.rect_x_end)
        self.y_map = int(self.y / self.rect_y_end)
        try:
            if map[self.y_map][self.x_map] == 1:
                self.x = self.old_x
                self.y = self.old_y
                return False
        except IndexError:
            self.x = self.old_x
            self.y = self.old_y
            return False
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.rect_x_end, self.rect_y_end))
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_direction(self):
        return self.dir
