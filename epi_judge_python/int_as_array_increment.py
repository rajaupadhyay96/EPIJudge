from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    res = []
    rem = 1

    i = len(A)-1
    while i >= 0:
        summed_digit = A[i]+rem
        res.append(summed_digit % 10)
        rem = summed_digit // 10
        i -= 1

    if rem:
       res.append(rem)

    return res[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
