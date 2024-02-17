from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    if len(s) == 1:
        return True
    l = 0
    r = len(s)-1

    while l <= r:
        if s[l].isalnum() and s[r].isalnum():
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        elif not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1

    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
