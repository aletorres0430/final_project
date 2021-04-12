from itertools import cycle
from random import random

import pygame

WIDTH = 1000
HEIGHT = 750
FPS = 60
TITLE = "Conway's Game of Life"
TILESIZES = cycle([8, 16, 32, 64])
TILESIZE = next(TILESIZES)
GENERATIONS_PER_SECOND = 10
RANDOM_CHANCE_TO_ALIVE_CELL = 0.25

LEFT = 0
RIGHT = 2

