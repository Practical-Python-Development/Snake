import random
import pygame

from board import Board
from config import COLOR_FOOD


class Food:
    def __init__(self, board: Board) -> None:
        """
        Create new food at a random position in the grid.

        Args:
            board: Reference to the board to query boundaries.
        """
        self.board = board
        self.position: tuple[int, int] = self.random_position()

    def random_position(self) -> tuple[int, int]:
        """Calculates a random position for the food within the board."""
        x = random.randrange(0, self.board.cols)
        y = random.randrange(0, self.board.rows)
        return x, y

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the food on the board."""
        x, y = self.position
        rect = pygame.Rect(
            x * self.board.block_size,
            y * self.board.block_size,
            self.board.block_size,
            self.board.block_size,
        )
        pygame.draw.rect(surface, COLOR_FOOD, rect)
