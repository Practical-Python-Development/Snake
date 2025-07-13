import sys
import pygame
from board import Board, Food

COLS, ROWS = 30, 30
BLOCK_SIZE = 20
FPS = 10

def show_start_screen(screen):
    """Shows a start screen and the snake do not start from alone."""
    font = pygame.font.SysFont(None, 36)
    text_surf = font.render("Press any arrow key to start", True, (255, 255, 255))
    text_rect = text_surf.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(text_surf, text_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return (0,1)
                elif event.key == pygame.K_DOWN:
                    return (0,1)
                elif event.key == pygame.K_LEFT:
                    return (-1,0)
                elif event.key == pygame.K_RIGHT:
                    return (1,0)


def show_game_over(screen):
    """shows game over on the screens and ends the game"""
    font_big = pygame.font.SysFont(None, 48)
    font_small = pygame.font.SysFont(None, 30)
    text_surf = font_big.render("Game Over", True, (255, 0, 0))
    text_restart = font_small.render("Press SPACE to restart or X to end", True, (255, 255, 255))
    rect = text_surf.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2-20))
    rect_restart = text_restart.get_rect(center=(COLS*BLOCK_SIZE//2,ROWS*BLOCK_SIZE//2+20))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(text_surf, rect)
        screen.blit(text_restart, rect_restart)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key in (pygame.K_x, pygame.K_ESCAPE):
                    return False

def main():
    """Starts the Snake game, initiates Pygame and executes the main loop.

    Opens the window, initializes game state and processes
    input, movement and drawing in each loop iteration.
    """
    pygame.init()
    screen = pygame.display.set_mode((COLS * BLOCK_SIZE, ROWS * BLOCK_SIZE))
    clock = pygame.time.Clock()
    board = Board(COLS, ROWS, BLOCK_SIZE)

    while True:
        direction = show_start_screen(screen)

        head = (COLS // 2, ROWS // 2)
        snake = [
            head,
            (head[0] - direction[0], head[1] - direction[1])
        ]
        food = Food(board)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if direction == (0,1):
                            running = False
                            break
                        direction = (0,-1)
                    elif event.key == pygame.K_DOWN:
                        if direction == (0,-1):
                            running = False
                            break
                        direction = (0,1)
                    elif event.key == pygame.K_LEFT:
                        if direction == (1,0):
                            running = False
                            break
                        direction = (-1,0)
                    elif event.key == pygame.K_RIGHT:
                        if direction == (-1,0):
                            running = False
                            break
                        direction = (1,0)
                    elif event.key in (pygame.K_x, pygame.K_ESCAPE):
                        pygame.quit()
                        sys.exit()

            if not running:
                break

            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = (head_x + dx, head_y + dy)

            #Collision
            if not (0 <= new_head[0] < COLS and 0 <= new_head[1] < ROWS):
                break
            if new_head in snake:
                break

            snake.insert(0, new_head)

            #Food
            if new_head == food.position:
                food = Food(board)
            else:
                snake.pop()

            board.draw(screen)
            food.draw(screen)
            for x, y in snake:
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, (0, 255, 0), rect)

            pygame.display.flip()
            clock.tick(FPS)

        if not show_game_over(screen):
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()