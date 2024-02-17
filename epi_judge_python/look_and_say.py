from test_framework import generic_test


def look_and_say(n: int) -> str:
    # 1, 11, 21, 1211, 111221, 312211

    res = ["1"]

    def _get_new_str(last_str):
        _tmp = []
        curr = 0
        len_s = len(last_str)

        while curr < len_s:
            r = curr
            while r < len_s and last_str[r] == last_str[curr]:
                r += 1
            _tmp.append(str(r-curr)+str(last_str[curr]))
            curr = r

        return "".join(_tmp)

    for _ in range(n-1):
        last = res[-1]
        res.append(_get_new_str(last))

    return res[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
