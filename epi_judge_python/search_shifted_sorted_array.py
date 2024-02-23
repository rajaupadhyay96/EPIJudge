from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    res = 0
    l = 0
    r = len(A)-1

    while l <= r:
        mid = l + (r-l)//2

        if A[mid] < A[res]:
            res = mid

        if A[mid] < A[r]:
            r = mid - 1
        else:
            l = mid + 1

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
