from typing import List

from test_framework import generic_test
from functools import cache

def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    
    res = 0

    def _find(score, idx):
        nonlocal res
        if score == 0:
            res += 1
            return
        if score < 0:
            return
        
        for curr_idx, play in enumerate(individual_play_scores[idx:], idx):
            _find(score-play, curr_idx)

    _find(final_score, 0)

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
