from test_framework import generic_test


def square_root(k: int) -> int:
    if k == 1:
        return 1
    
    l = 0
    r = k//2

    maxSoFar = 0

    while l <= r:
        mid = l + (r-l)//2

        if mid ** 2 <= k:
            maxSoFar = max(maxSoFar , mid)
            l = mid + 1
        else:
            r = mid - 1

    return maxSoFar
        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
