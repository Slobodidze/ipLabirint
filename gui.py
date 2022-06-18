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

class button:
    def __init__(self,screen,x,y,w,h,text,color,color_text = (255,255,255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.font = pygame.font.SysFont("Arial",20)
        self.screen = screen
        self.color_text = color_text
    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        text = self.font.render(self.text,1,self.color_text)
        self.screen.blit(text,(self.x+self.w/2-text.get_width()/2,self.y+self.h/2-text.get_height()/2))
    def is_clicked(self,pos):
        if pos[0] > self.x and pos[0] < self.x+self.w and pos[1] > self.y and pos[1] < self.y+self.h:
            return True
        else:
            return False


