import pygame
import random

# parameters of the window and game are set
TITLE = "Game of Life"
WIDTH = 1000
HEIGHT = 750
FPS = 60
TILESIZE = 12
GENERATIONS_PER_SECOND = 10

#RGB codes for black and white
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#setting up the grid and cells which are the main sprites of the game
class Cell(pygame.sprite.Sprite):
    #this function makes the grid of cells
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.off()

    #defines the cells when they are dead
    def off(self, color=BLACK):
        self.alive = False
        self.image.fill(color)

    #defines cell when they are alive
    def on(self, color=WHITE):
        self.alive = True
        self.image.fill(color)
        self.color = color

    #this was put in to keep a cell defined once it is in a stagnant state
    #meaning by the rules of the game the cell will stay alive because there are no cells around it
    #to make it change
    def survive(self, color=WHITE):
        self.alive = True
        self.color = WHITE
        self.image.fill(self.color)

#main code for the game itself
class Game:
    #initializes game and python window
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.next_generation_event = pygame.USEREVENT+1
        pygame.time.set_timer(self.next_generation_event, int(1000/GENERATIONS_PER_SECOND))

    #draws grid out on the window based on the tilesize, height, and width defined previously
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))

    #displays empty grid onto the window
    #all cells start off as dead
    def draw(self):
        self.all_sprites.draw(self.screen)
        if self.show_grid:
            self.draw_grid()
        pygame.display.flip()

    #this function allows user to randomly mix up grid
    def random_grid(self):
        for x in range(self.gridwidth):
            for y in range(self.gridheight):
                #each cell in the grid is assigned a randomly generated number between 0-1
                #if number of the cell is less than .25 then it will be defined as alive
                #allows for about 1/4 of the cells to be turned on when randomly mixing grid
                if random.random() < .25:
                    self.cells[x][y].on(self.color)
                #any cell assigned a number greater than .25 is defined as dead
                else:
                    self.cells[x][y].off()
    
    #this function is defininf all the parameters of the game interface
    def new(self):
        #grid wight and height
        self.gridwidth = int(WIDTH / TILESIZE)
        self.gridheight = int(HEIGHT / TILESIZE)
        #grid starts off paused
        #when you add live cells they won't begin the rules because grid is preset as paused
        #once user is ready they are able to unpause
        self.pause = True
        self.show_grid = True
        #defines color of the live cells as white (defined at the beginning)
        self.color = WHITE
        self.gps = GENERATIONS_PER_SECOND
        self.all_sprites = pygame.sprite.Group()
        self.cells = []
        #goes through all the cells in the x range then y range to define them
        for x in range(self.gridwidth):
            self.cells.append([])
            for y in range(self.gridheight):
                self.cells[x].append(Cell(self, x, y))
        self.previous_click, self.previous_x, self.previous_y = None, None, None

    #runs the game based on the parameters defined already
    def run(self):
        while True:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    #function to quit game when user wants to
    def quit(self):
        pygame.quit()

    #rules of the game begin here
    def next_generation(self):
        # this list will store the locations of cells that should be turned off
        killgrid = []
        # this list will store the locations of cells that should be turned on
        livegrid = []
        # These for loops iterate through every cell in the grid
        for x in range(self.gridwidth - 1):
            for y in range(self.gridheight - 1):
                # num_alive stores the number of live cells around each target cell
                num_alive = 0
                # iterates through the surrounding 8 cells from top left to bottom right, moving down the y values first
                for h in range(x-1, x+2):
                    for v in range(y-1, y+2):
                        # the middle cell is skipped in the 3x3 grid around the cell because that is not part of the surroundings
                        if (x,y) != (h,v):
                            if self.cells[h][v].alive:
                                # if the cell in the surroundings is on, increment num_alive
                                num_alive += 1
                # if the cell is surrounded by exactly 3 live cells, it will be turned on
                if num_alive == 3:
                    livegrid.append([x, y])
                # if the cell is surrounded by exactly 2 live cells, nothing happens to it
                # otherwise, the cell dies
                elif num_alive != 2:
                    killgrid.append([x, y])
        
        # cells that were marked for death are turned off
        for kcoordinate in killgrid:
            self.cells[kcoordinate[0]][kcoordinate[1]].off(BLACK)
        # cells that were marked for life are turned on
        for lcoordinate in livegrid:
            self.cells[lcoordinate[0]][lcoordinate[1]].on(self.color)
        
    #function for all the key presses/events in the game
    def events(self):
        for event in pygame.event.get():
            #game quits when you hit the red circle at top right of window
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                #game quits when you hit escape
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    self.quit()
                #pause value of the game is changed when you hit space
                #when window opens pause = TRUE, pressing the space bar will switch the value
                #of pause between TRUE and FALSE
                #when pause is FALSE the game will be running
                if event.key == pygame.K_SPACE:
                    self.pause = not(self.pause)
                #grid is randomized when you hit r
                if event.key == pygame.K_r:
                    self.random_grid()

            #gets x and y position of mouse to respond when you click
            click = pygame.mouse.get_pressed()
            x, y = pygame.mouse.get_pos()
            x = int(x / TILESIZE)
            y = int(y / TILESIZE)

            if (click, x, y) != (self.previous_click, self.previous_x, self.previous_y):
                #click[0] defines a normal left click on mouse/trackpad
                #clicking on a cell will turn it on
                if click[0] and not self.cells[x][y].alive:
                    self.cells[x][y].on(self.color)
                #clcik[2] defines a right click on mouse/trackpad
                #right clicking on a cell will turn it off
                elif click[2] and self.cells[x][y].alive:
                    self.cells[x][y].off(BLACK)
            #generations continue to run when the game is not paused
            if event.type == self.next_generation_event and not self.pause:
                self.next_generation()
            


g = Game()
#calls entire game class
while True:
    g.new()
    g.run()