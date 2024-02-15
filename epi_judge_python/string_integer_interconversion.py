from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string

def int_to_string(x: int) -> str:        
    res = []
    sign = ""
    if x < 0:
        sign = "-"
        x = abs(x)

    while True:
        res.append(str(x%10))
        x //= 10
        if not x:
            break

    res = res[::-1]
    res = sign + "".join(res)
    return res


def string_to_int(s: str) -> int:
    sign = +1
    if s[0] == "+":
        s = s[1:]
    if s[0] == "-":
        sign = -1
        s = s[1:]

    res = 0

    for idx, int_char in enumerate(s[::-1]):
        res += (10**idx)*string.digits.index(int_char)

    return res * sign


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
