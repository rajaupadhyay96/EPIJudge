from test_framework import generic_test


from collections import Counter
def can_form_palindrome(s: str) -> bool:
    if len(s) == 1:
        return True
    
    ctr = Counter(s)

    odd_count = 0
    for _, v in ctr.items():
        if v % 2 == 1:
            odd_count += 1

    return odd_count <= 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
