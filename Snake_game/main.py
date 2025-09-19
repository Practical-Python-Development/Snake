from pathlib import Path  # import order
import sys

import pygame

from board import Board, Food
# On module level "parts" (like imports, constants, functions, ...) are seperated by 2 new lines


COLS, ROWS = 30, 30
BLOCK_SIZE = 20
FPS = 10
HIGH_SCORE_FILE = Path("highscore.txt")  # use proper python build in libraries; HS could also be High School...


def load_highscore(path=HIGH_SCORE_FILE):  # typing, also return type
    """Loads the highscore from another file and gives it back."""
    if not path.is_file():  # first check for special cases
        return 0
    try:  # ... this reduces indentations here and therefor complexity
        with open(path, "r") as f:
            return int(f.read().strip())
    except ValueError:
        return 0


def save_highscore(score, path=HIGH_SCORE_FILE):  # typing
    """Write the new highscore to the file."""
    with open(path, "w") as f:
        f.write(str(score))


def show_start_screen(screen, highscore):  # typing, also return type
    """
    Shows the start screen and waits for an arrow key input.

    Draws notes on the screen:
      - Prompt to start with an arrow key
      - Display of the current high score
      - Reminder of the pause function (SPACE)

    Args:
        screen (pygame.Surface): Surface for rendering the start screen.
        highscore (int): The highest score so far to display.

    Returns:
        tuple[int, int]:
            Selected start direction as (dx, dy):
            (0, -1) for up, (0, 1) for down,
            (-1, 0) for left or (1, 0) for right.
    """
    font = pygame.font.SysFont(None, 36)
    font_big = pygame.font.SysFont(None, 50)
    text_head = font_big.render("Welcome to the SNAKE Game", True, (0, 255, 255))  # constants, you can make all settings as a constant tuple like this HEADER = ("Welcome to the SNAKE Game", True, (0, 255, 255) and use  like this font_big.render(*HEADER)
    text_surf = font.render("Press any arrow key to start", True, (255, 255, 255))  # constants
    text_high = font.render(f"Highscore: {highscore}", True, (255, 255, 0))  # constants
    text_pause = font.render("Press SPACE during game to pause", True, (200, 200, 200))  # constants
    text_rect_head = text_head.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2 - 175))  # Why 175? -> properly named constant
    text_rect = text_surf.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2 - 20))  # Why 20? -> properly named constant
    text_rect_high = text_high.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2 + 10))  # Why 10? -> properly named constant
    text_rect_pause = text_pause.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2 + 100))  # Why 100? -> properly named constant

    while True:
        screen.fill((0, 0, 0))
        screen.blit(text_head, text_rect_head)
        screen.blit(text_surf, text_rect)
        screen.blit(text_high, text_rect_high)
        screen.blit(text_pause, text_rect_pause)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return (0, -1)  # redundant parenthesis (PyCharm highlights this), whitespace, after ","
                elif event.key == pygame.K_DOWN:
                    return (0, 1)  # redundant parenthesis (PyCharm highlights this), whitespace, after ","
                elif event.key == pygame.K_LEFT:
                    return (-1, 0)  # redundant parenthesis (PyCharm highlights this), whitespace, after ","
                elif event.key == pygame.K_RIGHT:
                    return (1, 0)  # redundant parenthesis (PyCharm highlights this), whitespace, after ","


def pause(screen, clock):  #t yping
    """
    Pause the game and show the pause screen.

    Interrupts the game logic until the player continues via SPACE
    or ends the game via X or ESC. Draws a pause hint
    and a control instruction.

    Args:
        screen (pygame.Surface): Surface for rendering the pause screen.
        clock (pygame.time.Clock): Clock instance for frame rate control.

    Returns:
        None
    """
    font_big = pygame.font.SysFont(None, 48)  # 48 -> constant
    font_small = pygame.font.SysFont(None, 30)  # 30 -> constant, it might make sense to have a config.py with all the game config constants

    txt_pause = font_big.render("Paused", True, (255, 255, 255))  # constant
    txt_info = font_small.render("Press SPACE to resume or X to quit", True, (200, 200, 200))  # constant

    r_pause = txt_pause.get_rect(center=(COLS * BLOCK_SIZE // 2, ROWS * BLOCK_SIZE // 2 - 20))  # Why 20? -> properly named constant
    r_info = txt_info.get_rect(center=(COLS * BLOCK_SIZE // 2, ROWS * BLOCK_SIZE // 2 + 20))  # Why 20? -> properly named constant

    while True:
        screen.fill((0, 0, 0))
        screen.blit(txt_pause, r_pause)
        screen.blit(txt_info, r_info)
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.key in (pygame.K_x, pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()


def show_game_over(screen, score, highscore, new_highscore):  # typing, also return type
    """
    Game-Over-Screen: shows score, highscore and optionally
    a congratulations message, waits for SPACE (restart) or X (quit).

    Args:
        screen (pygame.Surface): Target surface.
        score (int): currently achieved score.
        highscore (int): current highscore (already updated if necessary).
        new_highscore (bool): True if score > previous highscore.
    Returns:
        bool: True = restart (SPACE), False = exit (X or ESC).
    """
    font_big = pygame.font.SysFont(None, 48)  # constant, see above
    font_small = pygame.font.SysFont(None, 30)  # constant, see above

    text_surf = font_big.render("Game Over", True, (255, 0, 0))  # constant, see above
    text_score = font_small.render(f"Your Score: {score}",True, (255, 255 ,255))  # constant, see above, whitespaces
    text_high = font_small.render(f"Highscore: {highscore}", True, (255, 255 ,0))  # constant, see above
    text_restart = font_small.render("Press SPACE to restart or X to end", True, (200, 200, 200))  # constant, see above, color tuples can be also defined just once as a constant and then be reused

    rect = text_surf.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2 - 60))  # Why 60? -> properly named constant, whitespaces
    rect_score = text_score.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2 - 20))  # Why 20? -> properly named constant
    rect_high = text_high.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2 + 10))  # Why 10? -> properly named constant
    rect_restart = text_restart.get_rect(center=(COLS*BLOCK_SIZE//2,ROWS*BLOCK_SIZE//2 + 50))  # Why 50? -> properly named constant, whitespaces

    if new_highscore:
        text_congrats = font_small.render(
            "Congratulations, you've cracked the high score!", True, (0, 255, 0)  # constant, see above
        )
        rect_congrats = text_congrats.get_rect(
            center=(COLS * BLOCK_SIZE // 2, ROWS * BLOCK_SIZE // 2 + 80)  # Why 50? -> properly named constant, whitespaces
        )

    while True:
        screen.fill((0, 0, 0))  # tuple as constant
        screen.blit(text_surf, rect)
        screen.blit(text_score, rect_score)
        screen.blit(text_high, rect_high)
        screen.blit(text_restart, rect_restart)

        if new_highscore:
            screen.blit(text_congrats, rect_congrats)

        pygame.display.flip()

        for event in pygame.event.get():
            # The event handling has a lot of duplicate code over the different "states". Can make functions for this? `handle_quit()`
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key in (pygame.K_x, pygame.K_ESCAPE):
                    return False


def play(screen, clock, board, initial_direction):  # typing, also return type
    """
    Executes a round of snake and returns the number of points scored.

    The function initializes the snake based on the passed
    start direction, processes inputs (arrow keys for direction, X or ESC to end),
    moves the snake, checks for collisions with the edge and itself,
    attracts food and records the game state and current score.

    Args:
        screen (pygame.Surface): The surface on which the game is rendered.
        clock (pygame.time.Clock): Controls the frame rate (FPS).
        board (Board): Instance of the game board for grid and background.
        initial_direction (tuple): Start direction of the snake as (dx, dy).

    Returns:
        int: Number of food pieces eaten (= score achieved).
    """
    # pretty massive function... Can you break it up and use some (protected) functions to handle parts of your logic?
    direction = initial_direction
    head = (COLS // 2, ROWS // 2)  # head_position?
    snake = [head,(head[0] - direction[0], head[1] - direction[1])]  # what is this? maybe rename,  restructure or comment
    food = Food(board)
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause(screen, clock)
                    pygame.event.clear()
                    break

            #elif event.type == pygame.KEYDOWN:  # remove
                if event.key == pygame.K_UP:
                    direction=(0,-1)  # whitespace
                elif event.key == pygame.K_DOWN:
                    direction=(0,1)  # whitespace
                elif event.key == pygame.K_LEFT:
                    direction=(-1,0)  # whitespace
                elif event.key == pygame.K_RIGHT:
                    direction=(1,0)  # whitespace
                elif event.key in (pygame.K_x, pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()


        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)

        # Collision
        if not (0 <= new_head[0] < COLS and 0 <= new_head[1] < ROWS):
            break
        if new_head in snake:
            break

        snake.insert(0, new_head)

        # Food
        if new_head == food.position:
            score += 1
            food = Food(board)
        else:
            snake.pop()

        board.draw(screen)
        food.draw(screen)

        for x, y in snake:
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (0, 255, 0), rect)  # color -> constant

        score_surf = pygame.font.SysFont(None, 24).render(f"Score: {score}", True, (255, 255, 255))  # constant, see above
        screen.blit(score_surf, (5, 5))  # Why (5, 5)? -> properly named constant

        pygame.display.flip()
        clock.tick(FPS)

    return score


def main():
    """Joins all building blocks together"""
    pygame.init()
    screen = pygame.display.set_mode((COLS * BLOCK_SIZE, ROWS * BLOCK_SIZE))
    clock = pygame.time.Clock()
    board = Board(COLS, ROWS, BLOCK_SIZE)
    highscore = load_highscore()

    while True:
        direction = show_start_screen(screen, highscore)

        score = play(screen, clock, board, direction)

        old_highscore = highscore

        if score > highscore:
            highscore = score
            save_highscore(highscore)
        new_high = score > old_highscore

        if not show_game_over(screen, score, highscore, new_high):  # Nice!
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
