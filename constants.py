FPS = 30 # frames per second to update the screen
WINDOW_WIDTH = 600  # width of the program's window, in pixels
WINDOW_HEIGHT = 600 # height in pixels

BOARD_WIDTH = 8 # how many columns in the board
BOARD_HEIGHT = 8 # how many rows in the board
GEM_IMAGE_SIZE = 64 # width & height of each space in pixels

# NUMGEMIMAGES is the number of gem types. You will need .png image
# files named gem0.png, gem1.png, etc. up to gem(N-1).png.
NUM_GEM_IMAGES = 7
SLEEP_OBSTACLE = NUM_GEM_IMAGES  # in the image array it will be the next object
MAD_OBSTACLE = NUM_GEM_IMAGES + 1
LOCATION_BOMB = MAD_OBSTACLE + 1
COLOR_BOMB = LOCATION_BOMB + 1
SLEEP_OBSTACLE_POINTS_NUM = 50
assert NUM_GEM_IMAGES >= 5 # game needs at least 5 types of gems to work

# NUMMATCHSOUNDS is the number of different sounds to choose from when
# a match is made. The .wav files are named match0.wav, match1.wav, etc.
NUM_MATCH_SOUNDS = 6

MOVE_RATE = 25 # 1 to 100, larger num means faster animations
DEDUCT_SPEED = 0.8 # reduces score by 1 point every DEDUCTSPEED seconds.

#             R    G    B
PURPLE    = (255,   0, 255)
LIGHTBLUE = (170, 190, 255)
BLUE      = (  0,   0, 255)
RED       = (255, 100, 100)
BLACK     = (  0,   0,   0)
BROWN     = ( 85,  65,   0)
HIGHLIGHT_COLOR = PURPLE # color of the selected gem's border
BG_COLOR = LIGHTBLUE # background color on the screen
GRID_COLOR = BLUE # color of the game board
GAME_OVER_COLOR = RED # color of the "Game over" text.
GAME_OVER_BG_COLOR = BLACK # background color of the "Game over" text.
SCORE_COLOR = BROWN # color of the text for the player's score

# The amount of space to the sides of the board to the edge of the window
# is used several times, so calculate it once here and store in variables.
X_MARGIN = int((WINDOW_WIDTH - GEM_IMAGE_SIZE * BOARD_WIDTH) / 2)
Y_MARGIN = int((WINDOW_HEIGHT - GEM_IMAGE_SIZE * BOARD_HEIGHT) / 2)

# constants for direction values
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

EMPTY_SPACE = -1 # an arbitrary, nonpositive value
ROW_ABOVE_BOARD = 'row above board' # an arbitrary, noninteger value

LOCATION_BOMB_NUM = 5 # Number of gem set that brings bomb
COLOR_BOMB_NUM = 4