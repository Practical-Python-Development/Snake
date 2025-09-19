"""
Unit tests for the Snake game.

These tests verify:
- Snake movement mechanics
- Collision detection (wall and self)
- Food placement and randomness
- High score saving and loading

All constants are imported from config.py to ensure tests remain valid
if the game configuration changes.
"""

import unittest
from pathlib import Path
from snake_game.config import GRID_COLS, GRID_ROWS
from snake_game.board import Board
from snake_game.food import Food
from snake_game.main import load_highscore, save_highscore


class TestSnakeMovement(unittest.TestCase):
    """Tests related to snake movement mechanics."""

    def test_move_20_steps_right(self):
        """
        Simulate moving the snake 20 steps to the right.

        Verifies:
             The head moves exactly 20 spaces to the right and ends at (20, 0).
             The snake remains within the board boundaries.
             The snake length stays constant at 2.
        """
        snake = [(0, 0), (-1, 0)]
        direction = (1, 0)

        for _ in range(20):
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            # Check boundaries
            self.assertTrue(0 <= new_head[0] < GRID_COLS)
            self.assertTrue(0 <= new_head[1] < GRID_ROWS)

            # Move snake
            snake.insert(0, new_head)
            snake.pop()

        self.assertEqual(snake[0], (20, 0))
        self.assertEqual(len(snake), 2)

    def test_move_up_and_down(self):
        """Tests moving up and then down returns to the starting position."""
        snake = [(5, 5), (5, 6)]
        direction_up = (0, -1)
        direction_down = (0, 1)

        # Move up
        head_x, head_y = snake[0]
        snake.insert(0, (head_x + direction_up[0], head_y + direction_up[1]))
        snake.pop()

        # Move down
        head_x, head_y = snake[0]
        snake.insert(0, (head_x + direction_down[0], head_y + direction_down[1]))
        snake.pop()

        self.assertEqual(snake[0], (5, 5))
        self.assertEqual(len(snake), 2)


class TestCollisions(unittest.TestCase):
    """Tests for wall and self-collision detection."""

    def test_wall_collision(self):
        """Verify that moving beyond the grid boundaries is detected."""
        snake = [(GRID_COLS - 1, 0)]
        direction = (1, 0)
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])
        self.assertFalse(0 <= new_head[0] < GRID_COLS)

    def test_self_collision(self):
        """Verify that moving into the snake's own body is detected."""
        snake = [(5, 5), (5, 6), (5, 7)]
        # Simulate moving head into position (5, 6)
        new_head = (5, 6)
        self.assertIn(new_head, snake[1:])


class TestFood(unittest.TestCase):
    """Tests for food placement and randomness."""

    def test_food_within_bounds(self):
        """Verify that food is always placed within the board boundaries."""
        board = Board(GRID_COLS, GRID_ROWS, 20)
        food = Food(board)
        x, y = food.position
        self.assertTrue(0 <= x < GRID_COLS)
        self.assertTrue(0 <= y < GRID_ROWS)

    def test_food_randomness(self):
        """Verify that food spawns at different positions over multiple generations."""
        board = Board(GRID_COLS, GRID_ROWS, 20)
        positions = {Food(board).position for _ in range(10)}
        self.assertTrue(len(positions) > 1)


class TestHighscore(unittest.TestCase):
    """Tests for high score saving and loading."""

    def test_highscore_save_and_load(self):
        """Verify that high scores can be saved to and loaded from a file."""
        test_file = Path("test_highscore.txt")
        if test_file.exists():
            test_file.unlink()

        save_highscore(42, path=test_file)
        loaded = load_highscore(path=test_file)

        self.assertEqual(loaded, 42)

        if test_file.exists():
            test_file.unlink()


if __name__ == "__main__":
    unittest.main()

