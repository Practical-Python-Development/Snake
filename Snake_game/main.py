import sys
import os
import pygame
from board import Board, Food

COLS, ROWS = 30, 30
BLOCK_SIZE = 20
FPS = 10
HS_FILE = "highscore.txt"

def load_highscore(path=HS_FILE):
    """Loads the highscore from another file and gives it back."""
    if os.path.isfile(path):
        try:
            with open(path, "r") as f:
                return int(f.read().strip())
        except ValueError:
            return 0
    return 0

def save_highscore(score, path=HS_FILE):
    """Wrotes the new highscore in the file."""
    with open(path, "w") as f:
        f.write(str(score))

def show_start_screen(screen, highscore):
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
    text_head = font_big.render("Welcome to the SNAKE Game", True, (0, 255, 255))
    text_surf = font.render("Press any arrow key to start", True, (255, 255, 255))
    text_high = font.render(f"Highscore: {highscore}", True, (255,255,0))
    text_pause = font.render("Press SPACE during game to pause", True, (200,200,200))
    text_recthead = text_head.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2-175))
    text_rect = text_surf.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2-20))
    text_recthigh = text_high.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2+10))
    text_rectpause = text_pause.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2+100))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(text_head, text_recthead)
        screen.blit(text_surf, text_rect)
        screen.blit(text_high, text_recthigh)
        screen.blit(text_pause, text_rectpause)
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

def pause(screen, clock):
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
    font_big = pygame.font.SysFont(None, 48)
    font_small = pygame.font.SysFont(None, 30)

    txt_pause = font_big.render("Paused", True, (255, 255, 255))
    txt_info = font_small.render("Press SPACE to resume or X to quit", True, (200, 200, 200))

    r_pause = txt_pause.get_rect(center=(COLS * BLOCK_SIZE // 2, ROWS * BLOCK_SIZE // 2 - 20))
    r_info = txt_info.get_rect(center=(COLS * BLOCK_SIZE // 2, ROWS * BLOCK_SIZE // 2 + 20))

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

def show_game_over(screen, score, highscore, new_highscore):
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
    font_big = pygame.font.SysFont(None, 48)
    font_small = pygame.font.SysFont(None, 30)

    text_surf = font_big.render("Game Over", True, (255, 0, 0))
    text_score = font_small.render(f"Your Score: {score}",True, (255,255,255))
    text_high = font_small.render(f"Highscore: {highscore}", True, (255,255,0))
    text_restart = font_small.render("Press SPACE to restart or X to end", True, (200, 200, 200))

    rect = text_surf.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2-60))
    rect_score = text_score.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2 - 20))
    rect_high = text_high.get_rect(center=(COLS*BLOCK_SIZE//2, ROWS*BLOCK_SIZE//2 + 10))
    rect_restart = text_restart.get_rect(center=(COLS*BLOCK_SIZE//2,ROWS*BLOCK_SIZE//2+50))

    if new_highscore:
        text_congrats = font_small.render(
            "Congratulations, you've cracked the high score!", True, (0, 255, 0)
        )
        rect_congrats = text_congrats.get_rect(
            center=(COLS * BLOCK_SIZE // 2, ROWS * BLOCK_SIZE // 2 + 80)
        )

    while True:
        screen.fill((0, 0, 0))
        screen.blit(text_surf, rect)
        screen.blit(text_score, rect_score)
        screen.blit(text_high, rect_high)
        screen.blit(text_restart, rect_restart)

        if new_highscore:
            screen.blit(text_congrats, rect_congrats)

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

def play(screen, clock, board, initial_direction):
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


    direction = initial_direction
    head = (COLS // 2, ROWS // 2)
    snake = [head,(head[0] - direction[0], head[1] - direction[1])]
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

            #elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction=(0,-1)
                elif event.key == pygame.K_DOWN:
                    direction=(0,1)
                elif event.key == pygame.K_LEFT:
                    direction=(-1,0)
                elif event.key == pygame.K_RIGHT:
                    direction=(1,0)
                elif event.key in (pygame.K_x, pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()


        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)

        #Cllision
        if not (0 <= new_head[0] < COLS and 0 <= new_head[1] < ROWS):
            break
        if new_head in snake:
            break

        snake.insert(0, new_head)

        #Food
        if new_head == food.position:
            score += 1
            food = Food(board)
        else:
            snake.pop()

        board.draw(screen)
        food.draw(screen)
        for x, y in snake:
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (0, 255, 0), rect)


        score_surf = pygame.font.SysFont(None, 24).render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, (5, 5))

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

        if not show_game_over(screen, score, highscore, new_high):
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()