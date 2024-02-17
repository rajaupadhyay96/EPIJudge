import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    if not s:
        return 0
    # first remove B's
    write_index = 0
    a_count = 0
    for i in range(size):
        if s[i] != "b":
            s[write_index] = s[i]
            write_index += 1
        if s[i] == "a":
            a_count += 1

    res = write_index + a_count
    ptr = write_index - 1
    write_index += a_count - 1
    
    while ptr >= 0:
        if s[ptr] == "a":
            s[write_index] = "d"
            s[write_index-1] = "d"
            write_index -= 2
        else:
            s[write_index] = s[ptr]
            write_index -= 1
        ptr -= 1
    
    return res

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
