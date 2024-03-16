#import
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
figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
field = [[0 for i in range(WIDTH)] for j in range(HEGHT)]

ANIM_COUNT, ANIM_SPEED, ANIM_LIMIT = 0, 60, 2000
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
            exit()
        if event in pygame.event == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1

            elif event.key == pygame.K_RIGHT:
                dx = 1

            elif event.key == pygame.K_DOWN:
                anim_limit = 100

            elif event.key == pygame.K_UP:
                rotate = True

    # move x
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break

    # move y
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
                for i in range(4):
                    field[figure_old[i].y][figure_old[i].x] = color
                figure, color = next_figure, next_color
                next_figure, next_color = deepcopy(choice(figures)), get_color()
                anim_limit = 2000


    # rotate
    center = figure[0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i] .x = center.x + y
            if not check_borders():
                figure = deepcopy(figure_old)


    #check lines
    line, lines = HEGHT - 1, 0
    for row in range(HEGHT - 1, -1, -1):
        count = 0
        for i in range(WIDTH):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < WIDTH:
            line -= 1
        else:
            anim_speed += 3
            lines += 1
    # score
    score += score[lines]

    # draw  grid
    [pygame.draw.rect(game_bg, (35, 35, 35), i_rect, 1) for i_rect in grid]

    # draw figure
    for i in range(4):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pygame.draw.rect(game_sc, color, figure_rect)

    # draw field
    for y, row in enumerate(field):
        for x, col in enumerate(row):
            if col:
                figure_rect.x, figure_rect.y = x * TILE, y * TILE
                pygame.draw.rect(game_sc, col, figure_rect)

    #draw next figure
    for i in range(4):
        figure_rect.x = next_figure.x * TILE + 380
        figure_rect.y = next_figure.y * TILE + 185
        pygame.draw.rect(sc, next_color, figure_rect)


























































