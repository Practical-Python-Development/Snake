import random  # import order
from itertools import product

import pygame
# On module level "parts" (like imports, constants, functions, ...) are seperated by 2 new lines


class Board:
    def __init__(
        self,
        cols=20,  # Why 20? -> properly named constant
        rows=20,  # Why 20? -> properly named constant
        block_size=20,  # Why 20? -> properly named constant
        bgcolor=(0, 0, 0),  # Why (0, 0, 0)? -> properly named constant
        gridcolor=(40, 40, 40),  # Why (40, 40, 40)? -> properly named constant
    ):
        """
        Initializes a grid playing field.

        Args:
         cols (int): Number of columns in the grid.
         rows (int): Number of rows in the grid.
         block_size (int): Pixel size of a single block.
         bgcolor (tuple): Background color as RGB tuple.
         gridcolor (tuple): Line color of the grid as RGB tuple.
        """
        # Maybe you can make some of your attributes and methods protected (name start with "_"), you can do this if it is only used within the board.
        self.cols = cols  # typing
        self.rows = rows  # typing
        self.block_size = block_size  # typing
        self.bgcolor = bgcolor  # typing
        self.gridcolor = gridcolor  # typing

    def draw(self, surface):  # typing
        """
        Draws the grid on a given Pygame surface.

        First fills the surface with the background color and then renders all grid lines.

         Args:
            surface (pygame.Surface): Target surface to draw on.
        """
        surface.fill(self.bgcolor)
        for x, y  in product(range(self.cols), range(self.rows)):  # reduce indentations and complexity
            rect = pygame.Rect(
                x * self.block_size,
                y * self.block_size,
                self.block_size,
                self.block_size
            )
            pygame.draw.rect(surface, self.gridcolor, rect, 1)


# Make a separate module for this
class Food:

    def __init__(self, board):
        """
        Create new lining at a random position in the grid.

        Args:
         board (Board): Reference to the board to query boundaries.
        """
        self.board = board  # typing
        self.position = self.random_position()  # typing

    def random_position(self):  # typing. also return typing
        """Calculates the food within the board."""
        x = random.randrange(0, self.board.cols)
        y = random.randrange(0, self.board.rows)
        return (x, y)  # PyCharm highlights "unnecessary parenthesis"

    def draw(self, surface):
        """Draw the food on the board."""
        x, y = self.position  # whitespace
        rect = pygame.Rect(
            x * self.board.block_size,
            y * self.board.block_size,
            self.board.block_size,
            self.board.block_size,
        )
        pygame.draw.rect(surface, (255, 0, 0), rect)  # color -> constant, maybe in config.py
