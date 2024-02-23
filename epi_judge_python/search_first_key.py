from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    l = 0
    r = len(A)-1

    while l <= r:
        mid = l + (r-l)//2 # to avoid overflow
        if A[mid] == k:
            if mid-1 >= 0 and A[mid-1] == k:
                r = mid-1
            else:
                return mid
        elif A[mid] < k:
            l = mid+1
        else:
            r = mid-1

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
