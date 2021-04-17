from itertools import cycle

import pygame
import time

WIDTH = 1000
HEIGHT = 750
FPS = 60
TITLE = "Game of Life"
TILESIZE = 12
GENERATIONS_PER_SECOND = 10
RANDOM_CHANCE_TO_ALIVE_CELL = 0.25


LEFT = 0
RIGHT = 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

userLiveRule1 = [1, 0, 0, 0, 0, 0, 0, 0]
userLiveRule2 = [0, 0, 0, 0, 0, 1, 0, 0]
userKillRule1 = [0, 0, 0, 0, 0, 1, 0, 0]

def getRules():
    addingRules = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    whiteSquare = pygame.image.load("White-Square.png").convert()
    whiteSquare = pygame.transform.scale(whiteSquare, (50, 50))
    screen.blit(whiteSquare, (50, 60))
    screen.blit(whiteSquare, (125, 60))
    screen.blit(whiteSquare, (200, 60))
    screen.blit(whiteSquare, (50, 135))
    screen.blit(whiteSquare, (200, 135))
    screen.blit(whiteSquare, (50, 210))
    screen.blit(whiteSquare, (125, 210))
    screen.blit(whiteSquare, (200, 210))
    
    pygame.display.flip()
    while addingRules:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    addingRules = False
                if event.key == pygame.K_ESCAPE:
                    self.quit()
            elif event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                if whiteSquare.get_rect().collidepoint(x - 50, y - 60):
                    print('clicked on image')

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

    def survive(self, color=WHITE):
        self.alive = True
        self.color = WHITE
        self.image.fill(self.color)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.next_generation_event = pygame.USEREVENT+1
        pygame.time.set_timer(self.next_generation_event, int(1000/GENERATIONS_PER_SECOND))

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))

    def draw(self):
        self.all_sprites.draw(self.screen)
        if self.show_grid:
            self.draw_grid()
        pygame.display.flip()
    
    def new(self):
        self.gridwidth = int(WIDTH / TILESIZE)
        self.gridheight = int(HEIGHT / TILESIZE)
        self.pause = True
        self.show_grid = True
        self.color = WHITE
        self.gps = GENERATIONS_PER_SECOND
        self.all_sprites = pygame.sprite.Group()
        self.cells = []
        for x in range(self.gridwidth):
            self.cells.append([])
            for y in range(self.gridheight):
                self.cells[x].append(Cell(self, x, y))
        self.previous_click, self.previous_x, self.previous_y = None, None, None

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def quit(self):
        pygame.quit()

    #start writing rules here
    def next_generation(self):
        killgrid = []
        livegrid = []
        for x in range(self.gridwidth -1):
            for y in range(self.gridheight -1):
                num_alive = 0
                surroundlist = []
                for h in range(x-1, x+2):
                    for v in range(y-1, y+2):
                        if (x,y) != (h,v):
                            if self.cells[h][v].alive:
                                surroundlist.append(1)
                            else:
                                surroundlist.append(0)
                if surroundlist == userLiveRule1:
                    livegrid.append([x, y])
                elif surroundlist == userLiveRule2:
                    livegrid.append([x, y])
                elif surroundlist == userKillRule1:
                    killgrid.append([x, y])
        for kcoordinate in killgrid:
            self.cells[kcoordinate[0]][kcoordinate[1]].off(BLACK)
        for lcoordinate in livegrid:
            self.cells[lcoordinate[0]][lcoordinate[1]].on(self.color)
        
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_SPACE:
                    self.pause = not(self.pause)

            click = pygame.mouse.get_pressed()
            x, y = pygame.mouse.get_pos()
            x = int(x / TILESIZE)
            y = int(y / TILESIZE)

            if (click, x, y) != (self.previous_click, self.previous_x, self.previous_y):
                if click[LEFT] and not self.cells[x][y].alive:
                    self.cells[x][y].on(self.color)
                elif click[RIGHT] and self.cells[x][y].alive:
                    self.cells[x][y].off(BLACK)
            if event.type == self.next_generation_event and not self.pause:
                self.next_generation()
            


g = Game()
getRules()
while True:
    g.new()
    g.run()