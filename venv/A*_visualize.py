import pygame, sys
import tkinter

screen = pygame.display.set_mode((800, 800))
class Square:
    def __init__(self, x, y):
        self.i = x
        self.j = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        self.obs = False
        self.closed = False
        self.value = 1

    def show(self, color, st):
        if self.closed == False :
            pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
            pygame.display.update()

    def path(self, color, st):
        pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
        pygame.display.update()

    def addNext(self, grid):
        i = self.i
        j = self.j
        if i < cols-1 and grid[self.i + 1][j].obs == False:
            self.neighbors.append(grid[self.i + 1][j])
        if i > 0 and grid[self.i - 1][j].obs == False:
            self.neighbors.append(grid[self.i - 1][j])
        if j < row-1 and grid[self.i][j + 1].obs == False:
            self.neighbors.append(grid[self.i][j + 1])
        if j > 0 and grid[self.i][j - 1].obs == False:
            self.neighbors.append(grid[self.i][j - 1])


cols = 100
grid = [0 for i in range(cols)]
row = 100
openSet = []
closedSet = []
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)
w = 800 / cols
h = 800 / row
cameFrom = []

# create 2d array
for i in range(cols):
    grid[i] = [0 for i in range(row)]

# Create Spots
for i in range(cols):
    for j in range(row):
        grid[i][j] = Square(i, j)


# Set start and end node
start = grid[12][5]
end = grid[3][6]
# SHOW RECT
for i in range(cols):
    for j in range(row):
        grid[i][j].show((255, 255, 255), 1)

for i in range(0,row):
    grid[0][i].show(grey, 0)
    grid[0][i].obs = True
    grid[cols-1][i].obs = True
    grid[cols-1][i].show(grey, 0)
    grid[i][row-1].show(grey, 0)
    grid[i][0].show(grey, 0)
    grid[i][0].obs = True
    grid[i][row-1].obs = True
