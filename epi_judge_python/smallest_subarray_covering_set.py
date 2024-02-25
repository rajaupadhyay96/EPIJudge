import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

from collections import Counter
def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    ctr = Counter(keywords)
    remaining = len(ctr)

    l = 0
    result = Subarray(-1, -1)
    for r, p in enumerate(paragraph):
        if p in keywords:
            ctr[p] -= 1
            if ctr[p] == 0:
                remaining -= 1

        while remaining == 0:
            if result == Subarray(-1, -1) or r - l < result.end - result.start:
                result = Subarray(l, r)
            left = paragraph[l]
            if left in keywords:
                ctr[left] += 1
                if ctr[left] > 0:
                    remaining += 1
            l += 1

    return result


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
