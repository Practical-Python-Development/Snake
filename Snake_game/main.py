import sys
import pygame
from board import Board

COLS, ROWS = 20, 20
BLOCK_SIZE = 20
FPS = 10

def main():
    """Starts the Snake game, initiates Pygame and executes the main loop.

    Opens the window, initializes game state and processes
    input, movement and drawing in each loop iteration.
    """
    pygame.init()
    screen = pygame.display.set_mode((COLS * BLOCK_SIZE, ROWS * BLOCK_SIZE))
    clock = pygame.time.Clock()
    board = Board(COLS, ROWS, BLOCK_SIZE)

    # start position of the snake
    snake = [(COLS // 2 + i, ROWS // 2) for i in range(3)]
    direction = (-1, 0)

    # reaction of the snake via key commands
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction=(0,1)
                elif event.key == pygame.K_DOWN:
                    direction=(0,-1)
                elif event.key == pygame.K_LEFT:
                    direction=(1,0)
                elif event.key == pygame.K_RIGHT:
                    direction=(-1,0)

        #How Snake should move and grow
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = ((head_x + dx) % COLS, (head_y + dy) % ROWS)
        snake.insert(0, new_head)
        snake.pop()

        board.draw(screen)
        for x, y in snake:
            rect = pygame.Rect(
                x * BLOCK_SIZE,
                y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE
            )
            pygame.draw.rect(screen, (0, 255, 0), rect)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()