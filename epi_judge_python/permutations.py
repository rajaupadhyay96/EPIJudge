from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
   
   def _find(lst):
        if len(lst) <= 1:
            return [lst]
        
        tmp = []
        for idx, i in enumerate(lst):
            perms = _find(lst[:idx] + lst[idx+1:])
            for p in perms:
                _res = [i] + p
                tmp.append(_res)

        return tmp
   
   return _find(A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
