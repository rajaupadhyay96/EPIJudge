from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    if not square_matrix:
        return []
    
    res = []

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    x, y = 0, 0
    curr_dir_idx = 0
    for _ in range(len(square_matrix)*len(square_matrix[0])):
        res.append(square_matrix[x][y])
        square_matrix[x][y] = "#"

        new_x = x+dirs[curr_dir_idx][0]
        new_y = y+dirs[curr_dir_idx][1]

        if new_x < 0 or new_x >= len(square_matrix) or new_y < 0 or new_y >= len(square_matrix[0]) or square_matrix[new_x][new_y] == "#":
            curr_dir_idx = (curr_dir_idx+1)%4
            new_x = x+dirs[curr_dir_idx][0]
            new_y = y+dirs[curr_dir_idx][1]

        x, y = new_x, new_y

    return res    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
