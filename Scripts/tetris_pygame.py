import pygame
from const import *

from copy import deepcopy
from random import choice, randrange

pygame.init()# активуємо бібліотеку pygame
sc = pygame.display.set_mode(RES)
game_sc = pygame.time.Clock()

grid = []
for x in range(WIDTH):
    for y in range(HEGHT):
        grid.append(pygame.Rect(x * TILE, y * TILE, TILE, TILE))
