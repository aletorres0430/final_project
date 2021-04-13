import pygame
import numpy as np

col_about_to_die = (200, 200, 225)
col_alive = (255, 255, 215)
col_background = (10, 10, 40)
col_grid = (30, 30, 60)

rulegrid = [[0, 0, 0],
            [1, 0, 1],
            [0, 0, 0]]

rulegrid = np.array(rulegrid)

def update(surface, cur, sz):
    nxt = np.zeros((cur.shape[0], cur.shape[1]))
    i = 0 #remove this

    for r, c in np.ndindex(cur.shape):
        num_alive = np.sum(cur[r-1:r+2, c-1:c+2]) - cur[r, c]

        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            col = col_about_to_die
        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
            nxt[r, c] = 1
            col = col_alive

        col = col if cur[r, c] == 1 else col_background
        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))
        i += 1
        surroundings = np.array([])
        surroundings = cur[r-1:r+1, c-1:c+1]
        #if i < 10:
            #print(surroundings)

    return nxt

def init(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    pattern = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);
    pos = (3,3)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    return cells

def main(dimx, dimy, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("John Conway's Game of Life")

    cells = init(dimx, dimy)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(col_grid)
        cells = update(surface, cells, cellsize)
        square1 = pygame.draw.rect(surface,(255, 255, 255),(200,150,45,45))
        pygame.draw.rect(surface,(255, 255, 255),(250,150,45,45))
        pygame.draw.rect(surface,(255, 255, 255),(300,150,45,45))
        pygame.draw.rect(surface,(255, 255, 255),(200,200,45,45))
        pygame.draw.rect(surface,(255, 255, 255),(250,200,45,45))
        pygame.draw.rect(surface,(255, 255, 255),(300,200,45,45))
        pygame.draw.rect(surface,(255, 255, 255),(200,250,45,45))
        pygame.draw.rect(surface,(255, 255, 255),(250,250,45,45))
        pygame.draw.rect(surface,(255, 255, 255),(300,250,45,45))
        pygame.display.update() 

if __name__ == "__main__":
    main(120, 90, 8)