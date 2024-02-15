from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    primes = []
    is_prime = [False, False] + [True]*(n-1)
    # F F T T T T T T T

    for idx, i in enumerate(is_prime):
        if i:
            primes.append(idx)

            for j in range(idx+idx, n+1, idx):
                is_prime[j] = False
    
    return primes



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
