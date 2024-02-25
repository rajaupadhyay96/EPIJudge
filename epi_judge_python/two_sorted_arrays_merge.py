from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    curr_write = m+n-1
    ptr_a = m-1
    ptr_b = n-1

    while ptr_a >= 0 and ptr_b >= 0:
        if A[ptr_a] >= B[ptr_b]:
            A[curr_write] = A[ptr_a]
            ptr_a -= 1
        else:
            A[curr_write] = B[ptr_b]
            ptr_b -= 1
        curr_write -= 1
    
    while ptr_a >= 0:
        A[curr_write] = A[ptr_a]
        curr_write -= 1
        ptr_a -= 1

    while ptr_b >= 0:
        A[curr_write] = B[ptr_b]
        curr_write -= 1
        ptr_b -= 1

    

def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
