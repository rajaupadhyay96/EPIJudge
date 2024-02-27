from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def _is_bin_tree(node, min_val, max_val):
    if not node:
        return True
    
    if min_val <= node.data <= max_val:
        return _is_bin_tree(node.left, min_val, node.data) and _is_bin_tree(node.right, node.data, max_val)
    
    return False


def _is_bin_tree(node):
    res = []

    def _rec(node):
        if not node:
            return 
        
        _rec(node.left)
        res.append(node.data)
        _rec(node.right)

    _rec(node)
    
    for idx, val in enumerate(res[1:], 1):
        if val < res[idx-1]:
            return False
    return True


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # return _is_bin_tree(tree, -float("inf"), float("inf"))
    return _is_bin_tree(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
