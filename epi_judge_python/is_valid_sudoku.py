from typing import List

from test_framework import generic_test

from collections import Counter

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # check every row and column
    ROWS = 9
    COLS = 9

    def validate_counter(counter):
        for num, count in counter.items():
            if count > 1 and num != 0:
                return False
        return True

    for row in range(ROWS):
        cntr = Counter(partial_assignment[row])
        is_valid = validate_counter(cntr)
        if not is_valid:
            return False
        
    for col in range(COLS):
        cntr = Counter([partial_assignment[i][col] for i in range(ROWS)])
        if not validate_counter(cntr):
            return False
        
    # validate each square
    for i in range(0, ROWS, 3):
        for j in range(0, COLS, 3):
            subgrid = [
                *partial_assignment[i][j:j+3],
                *partial_assignment[i+1][j:j+3],
                *partial_assignment[i+2][j:j+3]
            ]
            if not validate_counter(Counter(subgrid)):
                return False
            
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
