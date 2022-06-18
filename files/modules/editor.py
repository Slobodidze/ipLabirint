import pygame
import sys
import os
from gl import *
def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
from files.modules.color_picker import ColorPicker
clock = pygame.time.Clock()
# map_size = (int(input(">> Ширина ")), int(input(">> Высота ")))
cur_start = (0, 0)
cur_end = (0, 0)
def decode(text: str):
    message = []
    val = 0
    for letter in range(len(text)):
        if text[letter] != ' ':
            if len(message) == val:
                message.append(text[letter])
            else:
                message[val] += text[letter]
        else:
            message.append('')
            val += 1
    return message
def load_map_editor(screen,size,fps=30,map_size = (20,20),map_input=None):
    global cur_start, cur_end
    #map_size = (20, 20)
    rects_on_screen = size[0] / map_size[0]
    pos_x, pos_y = 0, 0
    if map_input == None:
        map = [[0] * map_size[0] for i in range(map_size[1])]
    else:
        map = map_input
    pos_map_x, pos_map_y = 0, 0
    cliked = False
    clicked_erase = False
    bg_color = (128, 128, 128)
    picker = ColorPicker(screen)
    start = (0,0)
    end = (0,0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    bg_color = picker.run()
                if event.key == pygame.K_ESCAPE:
                    return map, bg_color,start,end
                if event.key == pygame.K_j:
                    map[cur_start[1]][cur_start[0]] = 0
                    map[pos_map_y][pos_map_x] = 2
                    cur_start = (pos_map_x, pos_map_y)
                if event.key == pygame.K_k:
                    map[cur_end[1]][cur_end[0]] = 0
                    map[pos_map_y][pos_map_x] = 3
                    cur_end = (pos_map_x, pos_map_y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cliked = True
                if event.button == 3:
                    clicked_erase = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    cliked = False
                if event.button == 3:
                    clicked_erase = False
        if cliked:
            map[pos_map_y][pos_map_x] = 1
        if clicked_erase:
            map[pos_map_y][pos_map_x] = 0
        pos_x, pos_y = pygame.mouse.get_pos()
        pos_map_x, pos_map_y = int(pos_x // rects_on_screen), int(pos_y // rects_on_screen)
        screen.fill(bg_color)
        for y in range(len(map)):
            for x in range(len(map[y])):
                if map[y][x] == 1:
                    pygame.draw.rect(screen, (0, 0, 0),(x * rects_on_screen, y * rects_on_screen, rects_on_screen, rects_on_screen))
                if (x, y) == (pos_map_x, pos_map_y):
                    pygame.draw.rect(screen, (0, 255, 0),(x * rects_on_screen, y * rects_on_screen, rects_on_screen, rects_on_screen))
                if map[y][x] == 2:
                    start = (int(x),int(y))
                    pygame.draw.rect(screen, (255, 0, 0),(x * rects_on_screen, y * rects_on_screen, rects_on_screen,rects_on_screen))
                if map[y][x] == 3:
                    end = (int(x), int(y))
                    pygame.draw.rect(screen, (0, 0, 255),(x * rects_on_screen, y * rects_on_screen, rects_on_screen,rects_on_screen))
        pygame.display.update()
        clock.tick(fps)
