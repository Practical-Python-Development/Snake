import pygame

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