import pygame
from const import *

from copy import deepcopy
from random import choice, randrange

def check_borders():
    if not 0 < figure[i].x < WIDTH - 1:
       return  False
    elif figure[i].y > HEGHT - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True

def get_record():
    try:
        with open('record.txt', 'r') as f:
            return  f.readline()
    except FileNotFoundError:
        with open('record.txt', 'w') as f:
            f.write('0')

def set_record(record, score):
    rec = max(int(record), score)
    with open('record.txt', 'w') as f:
        f.write(str(rec))

pygame.init()# активуємо бібліотеку pygame
sc = pygame.display.set_mode(RES)
game_sc = pygame.time.Clock()

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(WIDTH) for y in range(HEGHT)]
figures = [[pygame.Rect(x + WIDTH // 2, y + 1,  1, 1) for x, y in fig_pos] for fig_pos in FIGURES_POSITIONS]
field = [[0 for i in range(WIDTH)] for j in range(HEGHT)]

anim_count, anim_speed, anim_limit = 0, 60, 2000
# anim_count, anim_speed, anim_limit = ANIM_COUNT, ANIM_SPEED, ANIM_LIMIT

bg = pygame.image.load('img/zoryane-nebo.jpg').convert()
game_bg = pygame.image.load('img/planet.jpg').convert()

main_font = pygame.font.Font('font/beer_money.ttf',70)
my_font = pygame.font.Font('font/GildiaTitulSlNormal.Ttf',50)
title_tetris = main_font.render('TETRIS',True, pygame.Color('purple'))
title_record = my_font.render('record :',True, pygame.Color('red'))
title_score = my_font.render('score:',True, pygame.Color('green'))

get_color = lambda:(randrange(50, 256), randrange(50, 256), randrange(50, 256))
figure, next_figure = deepcopy(choice(figures), deepcopy(choice(figures)))

score, lines = 0, 0
# score, lines = SCORE, LINES
score = {
        0: 0,
        1: 100,
        2: 300,
        3: 900,
        4: 2000

        }

while True:
    record = get_record()
    dx, rotate = 0, False
    sc.blit(bg,(0, 0))
    sc.blit(game_bg,(20, 20))
    game_sc.blit(game_bg, (0, 0))

    for i in range(lines):
        pygame.time.wait(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:




