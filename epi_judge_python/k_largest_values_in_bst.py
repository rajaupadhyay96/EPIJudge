from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    res = []

    def _rec(node):
        if not node:
            return
        
        _rec(node.right)
        if len(res) < k:
            res.append(node.data)
        _rec(node.left)

    _rec(tree)
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
