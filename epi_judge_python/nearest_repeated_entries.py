from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    dct = {}

    minRes = float("inf")

    for idx, word in enumerate(paragraph):
        if word in dct:
            lastIdx = dct[word]
            dct[word] = idx
            minRes = min(minRes, idx-lastIdx)
        else:
            dct[word] = idx

    if minRes == float("inf"):
        return -1
    return minRes
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
