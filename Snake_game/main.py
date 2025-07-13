import sys
import pygame
from board import Board, Food

COLS, ROWS = 20, 20
BLOCK_SIZE = 20
FPS = 10

def show_game_over(screen):
    """shows game over on the screens and ends the game"""
    font = pygame.font.SysFont(None, 48)
    text_surf = font.render("Game Over", True, (255, 0, 0))
    rect = text_surf.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2))
    screen.blit(text_surf, rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def main():
    """Starts the Snake game, initiates Pygame and executes the main loop.

    Opens the window, initializes game state and processes
    input, movement and drawing in each loop iteration.
    """
    pygame.init()
    screen = pygame.display.set_mode((COLS * BLOCK_SIZE, ROWS * BLOCK_SIZE))
    clock = pygame.time.Clock()
    board = Board(COLS, ROWS, BLOCK_SIZE)
    food = Food(board)

    # start position of the snake
    snake = [(COLS // 2, ROWS // 2), (COLS // 2 + 1, ROWS // 2)]
    direction = (-1, 0)

    # reaction of the snake via key commands
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction=(0,-1)
                elif event.key == pygame.K_DOWN:
                    direction=(0,1)
                elif event.key == pygame.K_LEFT:
                    direction=(-1,0)
                elif event.key == pygame.K_RIGHT:
                    direction=(1,0)

        #How Snake should move and grow with collision
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = ((head_x + dx), (head_y + dy))

        #Collision
        if not (0<= new_head[0] < COLS and 0 <= new_head[1] < ROWS):
            show_game_over(screen)
        if new_head in snake:
            show_game_over(screen)

        snake.insert(0, new_head)

        if new_head == food.position:
            food = Food(board)
        else:
            snake.pop()

        board.draw(screen)
        food.draw(screen)

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