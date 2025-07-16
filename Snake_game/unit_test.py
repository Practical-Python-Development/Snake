""" This skript tests the main Snake Programm"""

import unittest
import main
from board import Board, Food

COLS, ROWS = 30, 30

class TestSnakeMovement(unittest.TestCase):
    def test_move_20_steps_right(self):
        """
        Idee: Simuliere 20 Moves nach rechts und stelle sicher,
        dass die Schlange sich korrekt verschiebt und
        immer innerhalb der Grenzen bleibt.
        """
        # Start snake
        snake = [(0, 0), (-1, 0)]
        direction = (1, 0)

        for step in range(20):
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            self.assertTrue(new_head[0] < COLS)


        self.assertEqual(snake[0], (20, 0)) #runs into error in this line
        self.assertEqual(len(snake), 2)


if __name__ == "__main__":
    unittest.main()

