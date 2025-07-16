""" This skript tests the main Snake Programm"""

import unittest

COLS, ROWS = 30, 30

class TestSnakeMovement(unittest.TestCase):
    def test_move_20_steps_right(self):
        """
        Simuliere 20 Moves nach rechts und stelle sicher,
        dass die Schlange sich korrekt verschiebt und
        immer innerhalb der Grenzen bleibt.
        """
        # Start snake
        snake = [(0, 0), (-1, 0)]
        #direction = (1, 0)


        self.assertEqual(snake[0], (20, 0))
        self.assertEqual(len(snake), 2)


if __name__ == "__main__":
    unittest.main()

