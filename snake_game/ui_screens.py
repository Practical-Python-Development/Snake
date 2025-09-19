import sys
import pygame

from snake_game.config import (
    FONT_MEDIUM,
    FONT_BIG,
    FONT_SMALL,
    COLOR_TEXT_HEADER,
    COLOR_TEXT,
    COLOR_TEXT_HIGHLIGHT,
    COLOR_TEXT_SECONDARY,
    COLOR_TEXT_CONGRATS,
    COLOR_GAME_OVER,
    COLOR_BG,
    GRID_COLS,
    GRID_ROWS,
    BLOCK_SIZE,
    START_HEAD_OFFSET,
    START_TEXT_OFFSET,
    START_HIGHSCORE_OFFSET,
    START_PAUSE_OFFSET,
    PAUSE_TEXT_OFFSET,
    PAUSE_INFO_OFFSET,
    GAME_OVER_TITLE_OFFSET,
    GAME_OVER_SCORE_OFFSET,
    GAME_OVER_HIGHSCORE_OFFSET,
    GAME_OVER_RESTART_OFFSET,
    GAME_OVER_CONGRATS_OFFSET,
    FPS,
)


def show_start_screen(screen: pygame.Surface, highscore: int) -> tuple[int, int]:
    """
    Display the start screen and wait for the player to choose a starting direction.

    The screen shows:
      - A welcome header
      - Instructions to start the game
      - The current high score
      - A reminder about the pause function

    Args:
        screen: The game display surface.
        highscore: The current high score to display.

    Returns:
        A tuple (dx, dy) representing the initial movement direction:
        (0, -1) for up, (0, 1) for down, (-1, 0) for left, (1, 0) for right.
    """
    font = pygame.font.SysFont(None, FONT_MEDIUM)
    font_big = pygame.font.SysFont(None, FONT_BIG)

    text_head = font_big.render("Welcome to the SNAKE Game", True, COLOR_TEXT_HEADER)
    text_surf = font.render("Press any arrow key to start", True, COLOR_TEXT)
    text_high = font.render(f"Highscore: {highscore}", True, COLOR_TEXT_HIGHLIGHT)
    text_pause = font.render("Press SPACE during game to pause", True, COLOR_TEXT_SECONDARY)

    text_rect_head = text_head.get_rect(center=(GRID_COLS * BLOCK_SIZE // 2, GRID_ROWS * BLOCK_SIZE // 2 + START_HEAD_OFFSET))
    text_rect = text_surf.get_rect(center=(GRID_COLS * BLOCK_SIZE // 2, GRID_ROWS * BLOCK_SIZE // 2 + START_TEXT_OFFSET))
    text_rect_high = text_high.get_rect(center=(GRID_COLS * BLOCK_SIZE // 2, GRID_ROWS * BLOCK_SIZE // 2 + START_HIGHSCORE_OFFSET))
    text_rect_pause = text_pause.get_rect(center=(GRID_COLS * BLOCK_SIZE // 2, GRID_ROWS * BLOCK_SIZE // 2 + START_PAUSE_OFFSET))

    while True:
        screen.fill(COLOR_BG)
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
                    return 0, -1
                elif event.key == pygame.K_DOWN:
                    return 0, 1
                elif event.key == pygame.K_LEFT:
                    return -1, 0
                elif event.key == pygame.K_RIGHT:
                    return 1, 0


def pause(screen: pygame.Surface, clock: pygame.time.Clock) -> None:
    """
    Display the pause screen and wait for the player to resume or quit.

    The screen shows:
      - A "Paused" message
      - Instructions to resume or quit

    Args:
        screen: The game display surface.
        clock: The game clock for controlling frame rate during pause.

    Returns:
        None. Resumes the game when SPACE is pressed, exits if X or ESC is pressed.
    """
    font_big = pygame.font.SysFont(None, FONT_MEDIUM)
    font_small = pygame.font.SysFont(None, FONT_SMALL)

    txt_pause = font_big.render("Paused", True, COLOR_TEXT)
    txt_info = font_small.render("Press SPACE to resume or X to quit", True, COLOR_TEXT_SECONDARY)

    r_pause = txt_pause.get_rect(center=(GRID_COLS * BLOCK_SIZE // 2, GRID_ROWS * BLOCK_SIZE // 2 + PAUSE_TEXT_OFFSET))
    r_info = txt_info.get_rect(center=(GRID_COLS * BLOCK_SIZE // 2, GRID_ROWS * BLOCK_SIZE // 2 + PAUSE_INFO_OFFSET))

    while True:
        screen.fill(COLOR_BG)
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


def show_game_over(screen: pygame.Surface, score: int, highscore: int, new_highscore: bool) -> bool:
    """
    Display the game over screen and wait for the player to restart or quit.

    The screen shows:
      - "Game Over" message
      - The player's score
      - The current high score
      - Instructions to restart or quit
      - A congratulations message if a new high score was achieved

    Args:
        screen: The game display surface.
        score: The player's score from the last round.
        highscore: The current high score.
        new_highscore: True if the player achieved a new high score.

    Returns:
        True if the player chooses to restart (SPACE), False if they choose to quit (X or ESC).
    """
    font_big = pygame.font.SysFont(None, FONT_MEDIUM)
    font_small = pygame.font.SysFont(None, FONT_SMALL)

    text_surf = font_big.render("Game Over", True, COLOR_GAME_OVER)
    text_score = font_small.render(f"Your Score: {score}", True, COLOR_TEXT)
    text_high = font_small.render(f"Highscore: {highscore}", True, COLOR_TEXT_HIGHLIGHT)
    text_restart = font_small.render("Press SPACE to restart or X to end", True, COLOR_TEXT_SECONDARY)

    rect = text_surf.get_rect(center=(GRID_COLS * BLOCK_SIZE // 2, GRID_ROWS * BLOCK_SIZE // 2 + GAME_OVER_TITLE_OFFSET))
    rect_score = text_score.get_rect(center=(GRID_COLS * BLOCK_SIZE // 2, GRID_ROWS * BLOCK_SIZE // 2 + GAME_OVER_SCORE_OFFSET))
    rect_high = text_high.get_rect(center=(GRID_COLS * BLOCK_SIZE // 2, GRID_ROWS * BLOCK_SIZE // 2 + GAME_OVER_HIGHSCORE_OFFSET))
    rect_restart = text_restart.get_rect(center=(GRID_COLS * BLOCK_SIZE // 2, GRID_ROWS * BLOCK_SIZE // 2 + GAME_OVER_RESTART_OFFSET))

    if new_highscore:
        text_congrats = font_small.render("Congratulations, you've cracked the high score!", True, COLOR_TEXT_CONGRATS)
        rect_congrats = text_congrats.get_rect(center=(GRID_COLS * BLOCK_SIZE // 2, GRID_ROWS * BLOCK_SIZE // 2 + GAME_OVER_CONGRATS_OFFSET))

    while True:
        screen.fill(COLOR_BG)
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

