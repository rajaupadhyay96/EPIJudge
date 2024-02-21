from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:

    def _get_height(node):
        if not node:
            return 0
        
        left = _get_height(node.left)
        if left == -1:
            return -1
        right = _get_height(node.right)
        if right == -1:
            return -1

        if abs(left-right) > 1:
            return -1

        return max(left, right) + 1

    
    return _get_height(tree) != -1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
