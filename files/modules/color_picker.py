import pygame as pg
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class ColorPicker(object):
    def __init__(self, screen):
        self.done = False
        self.screen = screen
        self.font = pg.font.SysFont("Arial", 16)
        self.clock = pg.time.Clock()
        self.fps = 30

        self.square_size = 20
        self.colors = pg.color.THECOLORS
        self.labels = []
        self.color_names = []
        self.current_color = None

    def draw(self, surface):
        self.screen.fill(pg.Color("black"))
        square_size = 20
        left = 0
        top = 0
        for color in self.colors:
            pg.draw.rect(self.screen, self.colors[color],
                         (left, top, square_size, square_size))
            left += square_size
            if left + square_size > surface.get_width():
                top += square_size
                left = 0
        for label in self.labels:
            surface.blit(label[0], label[1])

    def update(self):
        self.labels = []
        left = 0
        top = 450
        if self.current_color:
            rgb_label = self.font.render("{}".format(self.current_color), True,
                                         pg.Color("white"), pg.Color("black"))
            rgb_rect = rgb_label.get_rect(topleft=(left, top))
            self.labels.append((rgb_label, rgb_rect))
            left += rgb_rect.width + 10
        for name in self.color_names:
            name_text = self.font.render("{0}".format(name), True,
                                         pg.Color("white"), pg.Color("black"))
            name_rect = name_text.get_rect(topleft=(left, top))
            left = name_rect.right + 20
            self.labels.append((name_text, name_rect))

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.current_color = self.screen.get_at(event.pos)
                '''self.color_names = []
                for name, value in self.colors.items():
                    if value == self.current_color:
                        self.color_names.append(name)'''

    def run(self):
        self.done = False
        self.current_color = None
        while not self.done:
            self.event_loop()
            self.update()
            self.draw(self.screen)
            pg.display.update()
            if self.current_color != None:
                return (self.current_color[0], self.current_color[1],self.current_color[2])

