from typing import Iterator, List

from test_framework import generic_test

import heapq

def online_median(sequence: Iterator[int]) -> List[float]:
    max_heap = []
    min_heap = []

    res = []

    for i in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, i))

        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        if len(min_heap) > len(max_heap):
            res.append(min_heap[0])
        else:
            res.append((min_heap[0] + -max_heap[0]) / 2)

    return res


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
