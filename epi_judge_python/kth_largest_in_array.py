from typing import List

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
import random
def find_kth_largest(k: int, A: List[int]) -> int:
    def quickselect(l, r, random_idx):
        ptr = l
        pivot_value = A[random_idx]
        A[random_idx], A[r] = A[r], A[random_idx]

        for i in range(l, r):
            if A[i] < pivot_value:
                A[ptr], A[i] = A[i], A[ptr]
                ptr += 1

        A[r], A[ptr] = A[ptr], A[r]
        return ptr
    
    l = 0
    r = len(A)-1

    while l <= r:
        pivot_idx = random.randint(l, r)
        new_pivot_idx = quickselect(l, r, pivot_idx)
        if k == len(A) - new_pivot_idx:
            return A[new_pivot_idx]
        elif k > len(A) - new_pivot_idx:
            r = new_pivot_idx - 1
        else:
            l = new_pivot_idx + 1

    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
