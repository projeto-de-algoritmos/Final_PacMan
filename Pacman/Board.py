from pygame import draw, Surface
import pygame
from colors import BLACK, WALL, STANDARD_COLOR
from random import randint

class Board():
    def __init__(self, width: int, height: int, horizontal: int, vertical: int, margin: int, standard_color: tuple) -> None:
        self.width = width
        self.height = height
        self.vertical = vertical
        self.horizontal = horizontal
        self.margin = margin
        self.color = standard_color
        self.maze_x = []
        self.maze_y = []
        self.squares_size = 25
        # Maze Squares
        self.squares = []
        self.free_spaces = []
        # directions to walk
        self.dx = [ -1, 1, 0,  0]
        self.dy = [  0, 0, 1, -1]
        self.grid = [[standard_color for i in range(vertical)] for j in range(horizontal)]

    def out_of_range(self, x: int, y: int) -> bool:
        """tells if x or y access self.grid invalid position
                Parameters:
                        x (int): x position in grid
                        y (int): y position in grid
                Returns:
                        True (bool):  is out of range
                        False (bool): is in range
        """
        return (x < 0 or y < 0 or x >= self.horizontal or y >= self.vertical)

    def draw_grid(self, screen: Surface) -> None:
        """draw grid to specific screen
                Parameters:
                        screen (Surface): game screen(
                Returns:
                        None
        """
        for row in range(self.horizontal):
            for column in range(self.vertical):
                draw.rect(screen,
                          self.grid[row][column],
                          [(self.margin + self.width) * (column) + self.margin,
                          (self.margin + self.height) * (row) + self.margin,
                          self.width,
                          self.height])

    def draw_maze(self, screen: Surface) -> None:
        """draw the current maze on the square list
                Parameters:
                        screen (Surface): game screen
                Returns:
                        None
        """
        for i in range(len(self.squares)):
            draw.rect(screen, WALL, self.squares[i])

    def free_space(self) -> None:
        """ Create a list of spaces that the player can move
                Parameters:
                        None
                Returns:
                        None
        """
        freex = []
        freey = []
        horizontal_size = 64
        vertical_size = 32
        for i in range(horizontal_size):
            freex.append(i*self.squares_size)
        for i in range(vertical_size):
            freey.append(i*self.squares_size)

        for i in range(len(freex)):
            for j in range(len(freey)):
                temp = pygame.Rect(freex[i], freey[j],
                                   self.squares_size, self.squares_size)
                self.free_spaces.append(temp)

        i = 0
        while i < len(self.free_spaces):
            for j in range(len(self.squares)):
                if pygame.Rect.colliderect(self.free_spaces[i], self.squares[j]):
                    self.free_spaces.pop(i)
                    i = i - 1
                    break
            i = i + 1
        
    def store_maze(self, screen: Surface) -> None:
        """store the current maze on the square list
                Parameters:
                        screen (Surface): game screen
                Returns:
                        None
        """
        edges = [(0, 0, self.squares_size, 800),
                (0, 0, 1600, self.squares_size),
                (1600 - self.squares_size, 0, self.squares_size, 800),
                (0, 800 - self.squares_size, 1600, self.squares_size)]
        for square in edges:
                self.squares.append(square)
        
        for i in range(len(self.maze_x)):
            edges = pygame.Rect((self.maze_x[i], self.maze_y[i], self.squares_size, self.squares_size))
            self.squares.append(edges)

    def maze_prim(self, x: int, y: int, screen: Surface) -> None:
        """draw maze in the screen based on prim's algorithm
                Parameters:
                        x (int): x screen coordinates
                        y (int): y screen coordinates
                        screen (Surface): game screen
                Returns:
                        None
        """
        check = [[False for i in range(self.vertical)] for j in range(self.horizontal)]
        vetX = []
        vetY = []
        # neighbors
        vetNX = []
        vetNY = []

        vetX.append(x)
        vetY.append(y)
        vetNX.append(0)
        vetNY.append(0)

        while vetX:

                n = randint(0, len(vetX) - 1)

                if self.out_of_range(vetX[n], vetY[n]) or check[vetX[n]][vetY[n]] == True:
                        vetX.pop(n)
                        vetY.pop(n)
                        vetNX.pop(n)
                        vetNY.pop(n)
                        continue

                posX = (self.margin + self.width) * (vetY[n]) + self.margin
                posY = (self.margin + self.height) * (vetX[n]) + self.margin
                self.maze_x.append(posX)
                self.maze_y.append(posY)

                posX = (self.margin + self.width) * (vetY[n] + vetNY[n]/2) + self.margin
                posY = (self.margin + self.height) * (vetX[n] + vetNX[n]/2) + self.margin
                self.maze_x.append(posX)
                self.maze_y.append(posY)

                check[vetX[n]][vetY[n]] = True
                
                for i in range(0, 4):
                        newX = vetX[n]+self.dx[i]
                        newY = vetY[n]+self.dy[i]
                        if not (self.out_of_range(newX, newY) or check[newX][newY] == True):
                                vetX.append(newX)
                                vetY.append(newY)
                                vetNX.append(self.dx[i])
                                vetNY.append(self.dy[i])