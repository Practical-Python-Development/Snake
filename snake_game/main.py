import sys
from pathlib import Path
import pygame

from snake_game.board import Board
from snake_game.food import Food
from snake_game.config import (
    GRID_COLS, GRID_ROWS, BLOCK_SIZE, FPS,
    COLOR_SNAKE, COLOR_TEXT, FONT_SCORE, SCORE_POS
)
from snake_game.ui_screens import show_start_screen, pause, show_game_over

HIGH_SCORE_FILE = Path("highscore.txt")


def load_highscore(path: Path = HIGH_SCORE_FILE) -> int:
    """
    Load the high score from a file.

    Args:
        path: Path to the high score file.

    Returns:
        The stored high score as an integer, or 0 if the file does not exist or is invalid.
    """
    if not path.is_file():
        return 0
    try:
        return int(path.read_text().strip())
    except ValueError:
        return 0


def save_highscore(score: int, path: Path = HIGH_SCORE_FILE) -> None:
    """
    Save the high score to a file.

    Args:
        score: The score value to save.
        path: Path to the high score file.
    """
    path.write_text(str(score))


def handle_input(direction: tuple[int, int], screen: pygame.Surface, clock: pygame.time.Clock) -> tuple[int, int]:
    """
    Handle player input events and return the updated movement direction.

    Args:
        direction: Current movement direction as (dx, dy).
        screen: The game display surface.
        clock: The game clock for controlling frame rate during pauses.

    Returns:
        The updated direction tuple, or the same direction if no change occurred.
        Exits the game if quit keys are pressed.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause(screen, clock)
                pygame.event.clear()
                return direction
            elif event.key == pygame.K_UP:
                return (0, -1)
            elif event.key == pygame.K_DOWN:
                return (0, 1)
            elif event.key == pygame.K_LEFT:
                return (-1, 0)
            elif event.key == pygame.K_RIGHT:
                return (1, 0)
            elif event.key in (pygame.K_x, pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
    return direction


def play(screen: pygame.Surface, clock: pygame.time.Clock, board: Board, initial_direction: tuple[int, int]) -> int:
    """
    Run a single round of the Snake game.

    Args:
        screen: The game display surface.
        clock: The game clock for controlling frame rate.
        board: The game board instance for drawing the grid.
        initial_direction: Starting movement direction as (dx, dy).

    Returns:
        The number of food items eaten (score) during the round.
    """
    direction = initial_direction
    head = (GRID_COLS // 2, GRID_ROWS // 2)
    snake = [head, (head[0] - direction[0], head[1] - direction[1])]
    food = Food(board)
    score = 0

    while True:
        direction = handle_input(direction, screen, clock)

        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)

        # Collision detection
        if not (0 <= new_head[0] < GRID_COLS and 0 <= new_head[1] < GRID_ROWS):
            break
        if new_head in snake:
            break

        snake.insert(0, new_head)

        # Food collection
        if new_head == food.position:
            score += 1
            food = Food(board)
        else:
            snake.pop()

        # Drawing
        board.draw(screen)
        food.draw(screen)

        for x, y in snake:
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, COLOR_SNAKE, rect)

        score_surf = pygame.font.SysFont(None, FONT_SCORE).render(f"Score: {score}", True, COLOR_TEXT)
        screen.blit(score_surf, SCORE_POS)

        pygame.display.flip()
        clock.tick(FPS)

    return score


def main() -> None:
    """
    Initialize and run the Snake game loop.

    Sets up the game window, loads the high score, and repeatedly:
    - Shows the start screen
    - Plays a game round
    - Updates and saves the high score if needed
    - Shows the game over screen
    Exits when the player chooses to quit.
    """
    pygame.init()
    screen = pygame.display.set_mode((GRID_COLS * BLOCK_SIZE, GRID_ROWS * BLOCK_SIZE))
    clock = pygame.time.Clock()
    board = Board(GRID_COLS, GRID_ROWS, BLOCK_SIZE)
    highscore = load_highscore()

    while True:
        direction = show_start_screen(screen, highscore)
        score = play(screen, clock, board, direction)

        old_highscore = highscore
        if score > highscore:
            highscore = score
            save_highscore(highscore)
        new_high = score > old_highscore

        if not show_game_over(screen, score, highscore, new_high):
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()

