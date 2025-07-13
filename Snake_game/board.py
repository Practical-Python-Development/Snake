import pygame
import random

class Board:
    def __init__(self, cols=20, rows=20, block_size=20,
                 bgcolor=(0, 0, 0), gridcolor=(40, 40, 40)):
        """Initializes a grid playing field.

        Args:
         cols (int): Number of columns in the grid.
         rows (int): Number of rows in the grid.
         block_size (int): Pixel size of a single block.
         bgcolor (tuple): Background color as RGB tuple.
         gridcolor (tuple): Line color of the grid as RGB tuple.
        """
        self.cols = cols
        self.rows = rows
        self.block_size = block_size
        self.bgcolor = bgcolor
        self.gridcolor = gridcolor

    def draw(self, surface):
        """Draws the grid on a given Pygame surface.

        First fills the surface with the background color and then renders all grid lines.

         Args:
            surface (pygame.Surface): Target surface to draw on.
        """
        surface.fill(self.bgcolor)
        for x in range(self.cols):
            for y in range(self.rows):
                rect = pygame.Rect(
                    x * self.block_size,
                    y * self.block_size,
                    self.block_size,
                    self.block_size
                )
                pygame.draw.rect(surface, self.gridcolor, rect, 1)

class Food:
    def __init__(self, board):
        """Creates new lining at a random position in the grid.

        Args:
         board (Board): Reference to the board to query boundaries.
        """
        self.board = board
        self.position = self.random_position()

    def random_position(self):
        """calculates the food within the board."""
        x = random.randrange(0, self.board.cols)
        y = random.randrange(0, self.board.rows)
        return(x, y)

    def draw(self, surface):
        """prints the food on the board"""
        x,y = self.position
        rect = pygame.Rect(x*self.board.block_size,
                           y*self.board.block_size,
                           self.board.block_size,
                           self.board.block_size
                           )
        pygame.draw.rect(surface, (255, 0, 0), rect)
