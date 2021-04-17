
import pygame


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
PBLACK = pygame.Color(0, 0, 0)
WHITE = (255, 255, 255)

userLiveRule1 = [0, 0, 0, 0, 0, 0, 0, 0]
# userLiveRule2 = [0, 0, 0, 0, 0, 1, 0, 0]
# userKillRule1 = [0, 0, 0, 0, 0, 1, 0, 0]

def getRules():
    addingRules = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    whiteSquare = pygame.image.load("White-Square.png").convert(24)
    whiteSquare.set_alpha(50)
    whiteSquare = pygame.transform.scale(whiteSquare, (50, 50))
    grid1coords = [(50, 60), (50, 135), (50, 210), (125, 60), (125, 210), (200, 60), (200, 135), (200, 210)]
    live11 = screen.blit(whiteSquare, grid1coords[0])
    live12 = screen.blit(whiteSquare, grid1coords[1])
    live13 = screen.blit(whiteSquare, grid1coords[2])
    live14 = screen.blit(whiteSquare, grid1coords[3])
    live15 = screen.blit(whiteSquare, grid1coords[4])
    live16 = screen.blit(whiteSquare, grid1coords[5])
    live17 = screen.blit(whiteSquare, grid1coords[6])
    live18 = screen.blit(whiteSquare, grid1coords[7])
    live1rects = [live11, live12, live13, live14, live15, live16, live17, live18]

    
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
                coordnumber = 0
                for coords in grid1coords:
                    if whiteSquare.get_rect().collidepoint(x - coords[0], y - coords[1]):
                        if userLiveRule1[coordnumber] == 1:
                            userLiveRule1[coordnumber] = 0
                            screen.fill(BLACK, live1rects[coordnumber])
                            live1rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                        else:
                            userLiveRule1[coordnumber] = 1
                            screen.fill(BLACK, live1rects[coordnumber])
                            whiteSquare.set_alpha(200)
                            live1rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                            whiteSquare.set_alpha(50)
                    coordnumber += 1
                # if whiteSquare.get_rect().collidepoint(x - 50, y - 60):
                #     if l11on:
                #         screen.fill(BLACK, live11)
                #         live11 = screen.blit(whiteSquare, (50, 60))
                #         pygame.display.flip()
                #         l11on = False
                #     else:
                #         screen.fill(BLACK, live11)
                #         whiteSquare.set_alpha(200)
                #         live11 = screen.blit(whiteSquare, (50, 60))
                #         pygame.display.flip()
                #         whiteSquare.set_alpha(50)
                #         l11on = True
                # elif whiteSquare.get_rect().collidepoint(x - 125, y - 60):
                #     if l12on:
                #         screen.fill(BLACK, live12)
                #         live12 = screen.blit(whiteSquare, (125, 60))
                #         pygame.display.flip()
                #         l12on = False
                #     else:
                #         screen.fill(BLACK, live12)
                #         whiteSquare.set_alpha(200)
                #         live12 = screen.blit(whiteSquare, (125, 60))
                #         pygame.display.flip()
                #         whiteSquare.set_alpha(50)
                #         l12on = True
                # elif whiteSquare.get_rect().collidepoint(x - 200, y - 60):
                #     if l13on:
                #         screen.fill(BLACK, live13)
                #         live13 = screen.blit(whiteSquare, (200, 60))
                #         pygame.display.flip()
                #         l13on = False
                #     else:
                #         screen.fill(BLACK, live13)
                #         whiteSquare.set_alpha(200)
                #         live13 = screen.blit(whiteSquare, (200, 60))
                #         pygame.display.flip()
                #         whiteSquare.set_alpha(50)
                #         l13on = True


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
                # elif surroundlist == userLiveRule2:
                #     livegrid.append([x, y])
                # elif surroundlist == userKillRule1:
                #     killgrid.append([x, y])
        # for kcoordinate in killgrid:
        #     self.cells[kcoordinate[0]][kcoordinate[1]].off(BLACK)
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