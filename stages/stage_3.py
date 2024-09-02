from stages.stage_2 import *
from constants import *


# STAGE 3
def check_patterns(board, row, col, patterns):
    for pattern in patterns:
        if (board[pattern[0][0] + row][pattern[0][1] + col] ==
                board[pattern[1][0] + row][pattern[1][1] + col] ==
                    board[pattern[2][0] + row][pattern[2][1] + col]):
            return True
    return False


def can_make_move(board):
    """
    Runs on every cell in the board and checks for pattern
    returns: Ture if there is a move to play and False if not
    """
    patterns = (((0, 1), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 0)),
                ((0, 0), (1, 1), (2, 0)),
                ((0, 1), (1, 0), (2, 1)),
                ((0, 0), (1, 0), (2, 1)),
                ((0, 0), (1, 1), (2, 1)),
                ((0, 0), (0, 2), (0, 3)),
                ((0, 0), (0, 1), (0, 3)),
                ((1, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (0, 2)),
                ((0, 0), (1, 1), (0, 2)),
                ((1, 0), (0, 1), (1, 2)),
                ((0, 0), (0, 1), (1, 2)),
                ((0, 0), (1, 1), (1, 2)),
                ((0, 0), (2, 0), (3, 0)),
                ((0, 0), (1, 0), (3, 0)))
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if check_patterns(board, row, col, patterns) or any(COLOR_BOMB in nested_list for nested_list in board):
                return True
    return False

