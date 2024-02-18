from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    if len(s) > len(t):
        return -1
    
    base = 26
    
    s_len = len(s)
    s_hash = 0
    for i in range(s_len):
        s_hash += base**(s_len-i-1) * ord(s[i])
    
    rolling_hash = 0
    for i in range(s_len):
        rolling_hash += base**(s_len-i-1) * ord(t[i])

    if rolling_hash == s_hash:
        return 0

    for i in range(s_len, len(t)):
        sub = (base**(s_len-1))*ord(t[i-s_len])
        rolling_hash = ((rolling_hash - sub) * base) + ord(t[i])

        if rolling_hash == s_hash:
            return i-s_len+1
        
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
