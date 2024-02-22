from typing import List

from test_framework import generic_test

import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    if not sorted_arrays:
        return None
    if len(sorted_arrays) == 1:
        return sorted_arrays[0]
    
    arr = sorted_arrays[0]
    heapq.heapify(arr)

    for array in sorted_arrays[1:]:
        for num in array:
            heapq.heappush(arr, num)

    res = []
    total_elements = len(arr)

    for _ in range(total_elements):
        res.append(heapq.heappop(arr))

    return res



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
