from stages.stage_3 import *


def find_surrounding_neighbors(row, col):
    """
    This function return a list of the exact location of the bomb surrounding neighbors
    :param row: row index of the cell to get its neighbors
    :param col: col index of the cell to get its neighbors
    :return: list of bomb neighbors locations on board
    """
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbors.append((row+i, col+j))
    return neighbors


    # for i in range(3):
    #     offset = -1
    #     for j in range(3):
    #         neighbor = []
    #         if (i != 1 and j!= 1):
    #             neighbor_col = col + offset
    #             neighbor.append(i)
    #             neighbor.append(neighbor_col)
    #         offset += 1
    #         if (i != 1 and j != 1):
    #             neighbors.append(neighbor)
    # for i in range(9):
    #     neighbor = []
    #     neighbor_col = 0
    #     neighbor_row = 0
    #     if i == 0:
    #         neighbor_col += -1
    #         neighbor_row += -1
    # return neighbors


def has_neighbors_in_location_sets(row, col, matched_gems):
    """
      This function checks if there are matches next to the checked location
      :param row: row index of the cell to check
      :param col: col index of the cell to check
      :param matched_gems: the matched gems set
      :return: True if there is a match next to the location and False if not
      """
    neighbors = find_surrounding_neighbors(row, col)
    for combination in matched_gems:
        for i in combination:
            if i in neighbors:
                return True
    return False
