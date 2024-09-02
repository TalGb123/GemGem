from constants import *


# STAGE 1
def get_gem_at(board, row, col):
    if (row >= BOARD_HEIGHT or col >= BOARD_WIDTH or row < 0 or col < 0):
        return None
    elif (0 <= row < BOARD_HEIGHT or 0 <= col < BOARD_WIDTH):
        return board[row][col]

