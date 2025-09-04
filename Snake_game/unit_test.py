""" This skript tests the main Snake program"""

import unittest

COLS, ROWS = 30, 30

class TestSnakeMovement(unittest.TestCase):

    def test_move_20_steps_right(self):
        """
        Tests the movement of the snake 20 steps to the right.

        Starts with a snake of length 2 like declared in main (head at (0,0)) and simulates
        20 steps in the direction of (1, 0). Verify that:

        1. the head moves exactly 20 spaces to the right and thus ends up at (20, 0).
        2. the snake always remains within the boundaries of the playing field (0 ≤ x < COLS, 0 ≤ y < ROWS)
        3. the length of the snake remains constant at 2 (no unwanted growth or shrinkage).
        """
        # Start snake  # unnecessary comment
        snake = [(0, 0), (-1, 0)]
        direction = (1, 0)

        for step in range(20):
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            self.assertTrue(0 <= new_head[0] < COLS)
            self.assertTrue(0 <= new_head[0] < ROWS)

            snake.insert(0, new_head)
            snake.pop()


        self.assertEqual(snake[0], (20, 0))  # runs into error in this line  # proper comment whitespacing
        self.assertEqual(len(snake), 2)


if __name__ == "__main__":
    unittest.main()
