# Game field
GRID_COLS: int = 30
GRID_ROWS: int = 30
BLOCK_SIZE: int = 20
FPS: int = 10

# Colors (RGB)
COLOR_BG: tuple[int, int, int] = (0, 0, 0)
COLOR_GRID: tuple[int, int, int] = (40, 40, 40)
COLOR_FOOD: tuple[int, int, int] = (255, 0, 0)
COLOR_SNAKE: tuple[int, int, int] = (0, 255, 0)
COLOR_TEXT: tuple[int, int, int] = (255, 255, 255)
COLOR_TEXT_HIGHLIGHT: tuple[int, int, int] = (255, 255, 0)
COLOR_TEXT_SECONDARY: tuple[int, int, int] = (200, 200, 200)
COLOR_TEXT_HEADER: tuple[int, int, int] = (0, 255, 255)
COLOR_TEXT_CONGRATS: tuple[int, int, int] = (0, 255, 0)
COLOR_GAME_OVER: tuple[int, int, int] = (255, 0, 0)

# Fonts
FONT_BIG: int = 50
FONT_MEDIUM: int = 36
FONT_SMALL: int = 30
FONT_SCORE: int = 24

# Positions
START_HEAD_OFFSET: int = -175
START_TEXT_OFFSET: int = -20
START_HIGHSCORE_OFFSET: int = 10
START_PAUSE_OFFSET: int = 100

PAUSE_TEXT_OFFSET: int = -20
PAUSE_INFO_OFFSET: int = 20

GAME_OVER_TITLE_OFFSET: int = -60
GAME_OVER_SCORE_OFFSET: int = -20
GAME_OVER_HIGHSCORE_OFFSET: int = 10
GAME_OVER_RESTART_OFFSET: int = 50
GAME_OVER_CONGRATS_OFFSET: int = 80

SCORE_POS: tuple[int, int] = (5, 5)
