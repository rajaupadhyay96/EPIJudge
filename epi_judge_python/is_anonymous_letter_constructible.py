from test_framework import generic_test


from collections import Counter
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    if len(magazine_text) < len(letter_text):
        return False
    
    letter_count = Counter(letter_text)
    magazine_count = Counter(magazine_text)

    for k, v in letter_count.items():
        if v > magazine_count.get(k, 0):
            return False
        
    return True
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
