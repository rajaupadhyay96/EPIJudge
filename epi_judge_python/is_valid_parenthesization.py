from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    brackets = "{}()[]"
    bracket_map = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    stack = []
    for bracket in s:
        if bracket not in brackets:
            return False
        if bracket in bracket_map:
            if not stack:
                return False
            prev_bracket = stack.pop()
            if prev_bracket != bracket_map[bracket]:
                return False
        else:
            stack.append(bracket)

    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
