from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    res = []
    ptr_a = 0
    ptr_b = 0

    while ptr_a < len(A) and ptr_b < len(B):
        last = res[-1] if res else None
        if A[ptr_a] == last:
            ptr_a += 1
        elif A[ptr_a] == B[ptr_b]:
            res.append(A[ptr_a])
            while ptr_b < len(B) and B[ptr_b] == res[-1]:
                ptr_b += 1
            while ptr_a < len(A) and A[ptr_a] == res[-1]:
                ptr_a += 1
        elif A[ptr_a] > B[ptr_b]:
            while ptr_b < len(B) and B[ptr_b] < A[ptr_a]:
                ptr_b += 1
        else:
            ptr_a += 1
    
    return res
        

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
