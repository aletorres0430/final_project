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

FONTSIZE = 15
FONT = 'arial'

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Cell(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.off()

    def off(self, color=BLACK):
        self.alive = False
        self.image.fill(color)

    def on(self, color=WHITE):
        self.alive = True
        self.image.fill(color)
        self.color = color

    def survive(self):
        r, g, b = self.color
        self.color = (r, g, b)
        self.image.fill(self.color)

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.new_generation_event = pygame.USEREVENT+1
        pygame.time.set_timer(self.new_generation_event, int(1000/GENERATIONS_PER_SECOND))

        self.menu_font = pygame.font.SysFont(FONT, FONTSIZE)