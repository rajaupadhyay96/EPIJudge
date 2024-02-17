from test_framework import generic_test

CHAR_INT = "0123456789ABCDEF"
INT_CHAR_MAP = {i: j for i, j in enumerate(CHAR_INT)}

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    int_val = 0
    sign = +1
    if num_as_string[0] == "+":
        num_as_string = num_as_string[1:]
    if num_as_string[0] == "-":
        sign = -1
        num_as_string = num_as_string[1:]

    for idx, s in enumerate(num_as_string[::-1]):
        int_val += (b1**idx)*CHAR_INT.index(s)
    
    res = []
    while True:
        rem=int_val%b2
        res.append(INT_CHAR_MAP[rem])
        int_val //= b2
        if not int_val:
            break

    if sign == -1:
        res.append("-")
    res = res[::-1]
    return "".join(res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
