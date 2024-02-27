from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    
    min_node = None

    def _find(node):
        nonlocal min_node
        
        if not node:
            return 
        
        if k >= node.data:
            _find(node.right)
        else:
            if not min_node:
                min_node = node
            else:
                if node.data < min_node.data:
                    min_node = node
            _find(node.left)

    _find(tree)

    return min_node


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
