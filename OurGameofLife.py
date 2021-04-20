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

# These lists store the custom rules that the user inputs
# each boolean represents an on or off cell in the surrounding
userLiveRule1 = [0, 0, 0, 0, 0, 0, 0, 0]
userLiveRule2 = [0, 0, 0, 0, 0, 0, 0, 0]
userLiveRule3 = [0, 0, 0, 0, 0, 0, 0, 0]
userKillRule1 = [0, 0, 0, 0, 0, 0, 0, 0]
userKillRule2 = [0, 0, 0, 0, 0, 0, 0, 0]
userKillRule3 = [0, 0, 0, 0, 0, 0, 0, 0]

#function runs at the beginning, displaying an interface for the user to input custom rules
def getRules():
    #the interface will stay up until addingRules becomes False, which happens when the user presses the Spacebar
    addingRules = True

    #opens the pygame window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    # whiteSquare is used to display the surround cells in the custom rule grids
    whiteSquare = pygame.image.load("White-Square.png").convert(24)
    # the square is made transparent, making it look dark gray
    whiteSquare.set_alpha(50)
    # The square is resized to 50x50
    whiteSquare = pygame.transform.scale(whiteSquare, (50, 50))
    # smallSquare is used to display the buttons that turn custom rule grids on and off
    smallSquare = pygame.transform.scale(whiteSquare, (24, 24))
    
    # These 6 blocks of code display the 6 custom rule grids
    
    # These coordinates are the locations of each surround cell in the custom rule grid
    live1coords = [(50, 60), (50, 135), (50, 210), (125, 60), (125, 210), (200, 60), (200, 135), (200, 210)]
    # These surfaces display each surround cell in the rule grid at its coordinate
    live11 = screen.blit(whiteSquare, live1coords[0])
    live12 = screen.blit(whiteSquare, live1coords[1])
    live13 = screen.blit(whiteSquare, live1coords[2])
    live14 = screen.blit(whiteSquare, live1coords[3])
    live15 = screen.blit(whiteSquare, live1coords[4])
    live16 = screen.blit(whiteSquare, live1coords[5])
    live17 = screen.blit(whiteSquare, live1coords[6])
    live18 = screen.blit(whiteSquare, live1coords[7])
    # This list stores the rectangles used to detect which squares are clicked on
    live1rects = [live11, live12, live13, live14, live15, live16, live17, live18]

    live2coords = [(350, 60), (350, 135), (350, 210), (425, 60), (425, 210), (500, 60), (500, 135), (500, 210)]
    live21 = screen.blit(whiteSquare, live2coords[0])
    live22 = screen.blit(whiteSquare, live2coords[1])
    live23 = screen.blit(whiteSquare, live2coords[2])
    live24 = screen.blit(whiteSquare, live2coords[3])
    live25 = screen.blit(whiteSquare, live2coords[4])
    live26 = screen.blit(whiteSquare, live2coords[5])
    live27 = screen.blit(whiteSquare, live2coords[6])
    live28 = screen.blit(whiteSquare, live2coords[7])
    live2rects = [live21, live22, live23, live24, live25, live26, live27, live28]

    live3coords = [(650, 60), (650, 135), (650, 210), (725, 60), (725, 210), (800, 60), (800, 135), (800, 210)]
    live31 = screen.blit(whiteSquare, live3coords[0])
    live32 = screen.blit(whiteSquare, live3coords[1])
    live33 = screen.blit(whiteSquare, live3coords[2])
    live34 = screen.blit(whiteSquare, live3coords[3])
    live35 = screen.blit(whiteSquare, live3coords[4])
    live36 = screen.blit(whiteSquare, live3coords[5])
    live37 = screen.blit(whiteSquare, live3coords[6])
    live38 = screen.blit(whiteSquare, live3coords[7])
    live3rects = [live31, live32, live33, live34, live35, live36, live37, live38]

    kill1coords = [(50, 460), (50, 535), (50, 610), (125, 460), (125, 610), (200, 460), (200, 535), (200, 610)]
    kill11 = screen.blit(whiteSquare, kill1coords[0])
    kill12 = screen.blit(whiteSquare, kill1coords[1])
    kill13 = screen.blit(whiteSquare, kill1coords[2])
    kill14 = screen.blit(whiteSquare, kill1coords[3])
    kill15 = screen.blit(whiteSquare, kill1coords[4])
    kill16 = screen.blit(whiteSquare, kill1coords[5])
    kill17 = screen.blit(whiteSquare, kill1coords[6])
    kill18 = screen.blit(whiteSquare, kill1coords[7])
    kill1rects = [kill11, kill12, kill13, kill14, kill15, kill16, kill17, kill18]

    kill2coords = [(350, 460), (350, 535), (350, 610), (425, 460), (425, 610), (500, 460), (500, 535), (500, 610)]
    kill21 = screen.blit(whiteSquare, kill2coords[0])
    kill22 = screen.blit(whiteSquare, kill2coords[1])
    kill23 = screen.blit(whiteSquare, kill2coords[2])
    kill24 = screen.blit(whiteSquare, kill2coords[3])
    kill25 = screen.blit(whiteSquare, kill2coords[4])
    kill26 = screen.blit(whiteSquare, kill2coords[5])
    kill27 = screen.blit(whiteSquare, kill2coords[6])
    kill28 = screen.blit(whiteSquare, kill2coords[7])
    kill2rects = [kill21, kill22, kill23, kill24, kill25, kill26, kill27, kill28]

    kill3coords = [(650, 460), (650, 535), (650, 610), (725, 460), (725, 610), (800, 460), (800, 535), (800, 610)]
    kill31 = screen.blit(whiteSquare, kill3coords[0])
    kill32 = screen.blit(whiteSquare, kill3coords[1])
    kill33 = screen.blit(whiteSquare, kill3coords[2])
    kill34 = screen.blit(whiteSquare, kill3coords[3])
    kill35 = screen.blit(whiteSquare, kill3coords[4])
    kill36 = screen.blit(whiteSquare, kill3coords[5])
    kill37 = screen.blit(whiteSquare, kill3coords[6])
    kill38 = screen.blit(whiteSquare, kill3coords[7])
    kill3rects = [kill31, kill32, kill33, kill34, kill35, kill36, kill37, kill38]

    grid1button = screen.blit(smallSquare, (138,300))
    grid2button = screen.blit(smallSquare, (438,300))
    grid3button = screen.blit(smallSquare, (738,300))
    grid4button = screen.blit(smallSquare, (138,700))
    grid5button = screen.blit(smallSquare, (438,700))
    grid6button = screen.blit(smallSquare, (738,700))
    
    # These booleans store whether each rule grid is on or off
    global grid1on, grid2on, grid3on, grid4on, grid5on, grid6on
    grid1on = False
    grid2on = False
    grid3on = False
    grid4on = False
    grid5on = False
    grid6on = False
    
    # displays the changes made to the screen
    pygame.display.flip()
    
    # This loop will continue until the user presses Spacebar, exiting the custom rule interface and proceding to the game
    while addingRules:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # if the Spacebar is pressed, exit the custom rule interface
                    addingRules = False
                if event.key == pygame.K_ESCAPE:
                    # if Escape is pressed, end the pygame window
                    self.quit()
            elif event.type == pygame.QUIT:
                # if the window close button is pressed, end the pygame window
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                coordnumber = 0

                # these for loops check if the surround cells in each grid were clicked on
                # iterates through all 8 surround cell coordinates the first rule grid to check if one was clicked on
                for coords in live1coords:
                    # if the cell was clicked, flip its on value and color
                    if whiteSquare.get_rect().collidepoint(x - coords[0], y - coords[1]):
                        if userLiveRule1[coordnumber] == 1:
                            # if it was on, turn its value and its color off
                            userLiveRule1[coordnumber] = 0
                            screen.fill(BLACK, live1rects[coordnumber])
                            live1rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                        else:
                            # if it was off, turn its value and its color on
                            userLiveRule1[coordnumber] = 1
                            screen.fill(BLACK, live1rects[coordnumber])
                            whiteSquare.set_alpha(200)
                            live1rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                            whiteSquare.set_alpha(50)
                    coordnumber += 1
                coordnumber = 0
                for coords in live2coords:
                    if whiteSquare.get_rect().collidepoint(x - coords[0], y - coords[1]):
                        if userLiveRule2[coordnumber] == 1:
                            userLiveRule2[coordnumber] = 0
                            screen.fill(BLACK, live2rects[coordnumber])
                            live2rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                        else:
                            userLiveRule2[coordnumber] = 1
                            screen.fill(BLACK, live2rects[coordnumber])
                            whiteSquare.set_alpha(200)
                            live2rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                            whiteSquare.set_alpha(50)
                    coordnumber += 1
                coordnumber = 0
                for coords in live3coords:
                    if whiteSquare.get_rect().collidepoint(x - coords[0], y - coords[1]):
                        if userLiveRule3[coordnumber] == 1:
                            userLiveRule3[coordnumber] = 0
                            screen.fill(BLACK, live3rects[coordnumber])
                            live3rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                        else:
                            userLiveRule3[coordnumber] = 1
                            screen.fill(BLACK, live3rects[coordnumber])
                            whiteSquare.set_alpha(200)
                            live3rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                            whiteSquare.set_alpha(50)
                    coordnumber += 1
                coordnumber = 0
                for coords in kill1coords:
                    if whiteSquare.get_rect().collidepoint(x - coords[0], y - coords[1]):
                        if userKillRule1[coordnumber] == 1:
                            userKillRule1[coordnumber] = 0
                            screen.fill(BLACK, kill1rects[coordnumber])
                            kill1rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                        else:
                            userKillRule1[coordnumber] = 1
                            screen.fill(BLACK, kill1rects[coordnumber])
                            whiteSquare.set_alpha(200)
                            kill1rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                            whiteSquare.set_alpha(50)
                    coordnumber += 1
                coordnumber = 0
                for coords in kill2coords:
                    if whiteSquare.get_rect().collidepoint(x - coords[0], y - coords[1]):
                        if userKillRule2[coordnumber] == 1:
                            userKillRule2[coordnumber] = 0
                            screen.fill(BLACK, kill2rects[coordnumber])
                            kill2rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                        else:
                            userKillRule2[coordnumber] = 1
                            screen.fill(BLACK, kill2rects[coordnumber])
                            whiteSquare.set_alpha(200)
                            kill2rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                            whiteSquare.set_alpha(50)
                    coordnumber += 1
                coordnumber = 0
                for coords in kill3coords:
                    if whiteSquare.get_rect().collidepoint(x - coords[0], y - coords[1]):
                        if userKillRule3[coordnumber] == 1:
                            userKillRule3[coordnumber] = 0
                            screen.fill(BLACK, kill3rects[coordnumber])
                            kill3rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                        else:
                            userKillRule3[coordnumber] = 1
                            screen.fill(BLACK, kill3rects[coordnumber])
                            whiteSquare.set_alpha(200)
                            kill3rects[coordnumber] = screen.blit(whiteSquare, coords)
                            pygame.display.flip()
                            whiteSquare.set_alpha(50)
                    coordnumber += 1
                    
                # these if statements check if an on/off button was clicked
                if grid1button.collidepoint(x, y):
                    # if the button was clicked, flip its on/off value
                    if grid1on:
                        #if it was on, turn its value and its color off
                        grid1on = False
                        screen.fill(BLACK, grid1button)
                        grid1button = screen.blit(smallSquare, (138,300))
                        pygame.display.flip()
                    else:
                        #if it was off, turn its value and its color on
                        grid1on = True
                        screen.fill(BLACK, grid1button)
                        smallSquare.set_alpha(200)
                        grid1button = screen.blit(smallSquare, (138,300))
                        pygame.display.flip()
                        smallSquare.set_alpha(50)
                if grid2button.collidepoint(x, y):
                    if grid2on:
                        grid2on = False
                        screen.fill(BLACK, grid2button)
                        grid2button = screen.blit(smallSquare, (438,300))
                        pygame.display.flip()
                    else:
                        grid2on = True
                        screen.fill(BLACK, grid2button)
                        smallSquare.set_alpha(200)
                        grid2button = screen.blit(smallSquare, (438,300))
                        pygame.display.flip()
                        smallSquare.set_alpha(50)
                if grid3button.collidepoint(x, y):
                    if grid3on:
                        grid3on = False
                        screen.fill(BLACK, grid3button)
                        grid3button = screen.blit(smallSquare, (738,300))
                        pygame.display.flip()
                    else:
                        grid3on = True
                        screen.fill(BLACK, grid3button)
                        smallSquare.set_alpha(200)
                        grid3button = screen.blit(smallSquare, (738,300))
                        pygame.display.flip()
                        smallSquare.set_alpha(50)
                if grid4button.collidepoint(x, y):
                    if grid4on:
                        grid4on = False
                        screen.fill(BLACK, grid4button)
                        grid4button = screen.blit(smallSquare, (138,700))
                        pygame.display.flip()
                    else:
                        grid4on = True
                        screen.fill(BLACK, grid4button)
                        smallSquare.set_alpha(200)
                        grid4button = screen.blit(smallSquare, (138,700))
                        pygame.display.flip()
                        smallSquare.set_alpha(50)
                if grid5button.collidepoint(x, y):
                    if grid5on:
                        grid5on = False
                        screen.fill(BLACK, grid5button)
                        grid5button = screen.blit(smallSquare, (438,700))
                        pygame.display.flip()
                    else:
                        grid5on = True
                        screen.fill(BLACK, grid5button)
                        smallSquare.set_alpha(200)
                        grid5button = screen.blit(smallSquare, (438,700))
                        pygame.display.flip()
                        smallSquare.set_alpha(50)
                if grid6button.collidepoint(x, y):
                    if grid6on:
                        grid6on = False
                        screen.fill(BLACK, grid6button)
                        grid6button = screen.blit(smallSquare, (738,700))
                        pygame.display.flip()
                    else:
                        grid6on = True
                        screen.fill(BLACK, grid6button)
                        smallSquare.set_alpha(200)
                        grid6button = screen.blit(smallSquare, (738,700))
                        pygame.display.flip()
                        smallSquare.set_alpha(50)

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
        for x in range(self.gridwidth -1):
            for y in range(self.gridheight -1):
                # creates a list of booleans that represents the on/off values of the surrounding 8 cells
                # this list will be compared to the custom rule lists to see if the cell should be killed or alive
                surroundlist = []
                # iterates through the surrounding 8 cells from top left to bottom right, moving down the y values first
                for h in range(x-1, x+2):
                    for v in range(y-1, y+2):
                        # the middle cell is skipped in the 3x3 grid around the cell because that is not part of the surroundings
                        if (x,y) != (h,v):
                            if self.cells[h][v].alive:
                                # if this surround cell is on, represent it as a 1 in the list
                                surroundlist.append(1)
                            else:
                                # if this surround cell is off, represent it as a 0 in the list
                                surroundlist.append(0)
                #if the cells around any target cell match live rule 1 then cell turns on
                if surroundlist == userLiveRule1 and grid1on:
                    livegrid.append([x, y])
                #if the cells around any target cell match live rule 2 then cell turns on
                elif surroundlist == userLiveRule2 and grid2on:
                    livegrid.append([x, y])
                #if the cells around any target cell match live rule 3 then cell turns on
                elif surroundlist == userLiveRule3 and grid3on:
                    livegrid.append([x, y])
                #if the cells around any target cell match kill rule 4 then cell turns off
                elif surroundlist == userKillRule1 and grid4on:
                    killgrid.append([x, y])
                #if the cells around any target cell match kill rule 5 then cell turns off
                elif surroundlist == userKillRule2 and grid5on:
                    killgrid.append([x, y])
                #if the cells around any target cell match kill rule 6 then cell turns off
                elif surroundlist == userKillRule3 and grid6on:
                    killgrid.append([x, y])
        for kcoordinate in killgrid:
            self.cells[kcoordinate[0]][kcoordinate[1]].off(BLACK)
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
                if event.key == pygame.K_ESCAPE:
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
getRules()
#calls entire game class and function for defining rules at the beginning
while True:
    g.new()
    g.run()