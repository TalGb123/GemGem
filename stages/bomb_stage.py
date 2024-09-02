from stages.obstacle_stage import *


def get_local_bomb_gems_to_remove(board, row, col):
    """
       This function return a list of the gems to remove after the local bomb
       :param board: the board game
       :param row, col: location of the bomb gem after swap
       :return: list of the neighbors locations on board
    """
    to_remove = []
    neighbors = find_surrounding_neighbors(row, col)
    for i in range(len(neighbors)):
        if get_gem_at(board, row, col) != None:
            to_remove.append((row, col))
    return to_remove


def get_new_board(board, matched_gems):
    """
        This function returns the updated board after moving away the matched gems locations
        :param matched_gems: the matched gems to remove.
        :param board: the game board
        :return: the updated board
    """
    if (len(matched_gems) == LOCATION_BOMB_NUM):
        for i in matched_gems:
            for j in matched_gems[i]:
                if (i != 0):
                    board[i][j] = EMPTY_SPACE
                else:
                    board[i][j] = LOCATION_BOMB
    elif (len(matched_gems) == COLOR_BOMB_NUM):
        for i in matched_gems:
            for j in matched_gems[i]:
                if (i != 0):
                    board[i][j] = EMPTY_SPACE
                else:
                    board[i][j] = COLOR_BOMB
    return board


def get_color_bomb_gems_to_remove(board, target_gem_kind):
    """
    This function gets go over the board and returns a list of all the identical gems to the target
    :param board: the board game
    :param target_gem_kind: the number of the targeted gem
    :return: list of gems to remove
    """
    gems_to_remove = []
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if board[row][col] == target_gem_kind:
                gems_to_remove.append((row, col))
    return gems_to_remove
