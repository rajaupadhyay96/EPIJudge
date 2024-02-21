from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []
    
    res = []
    visited = set([tree])

    stack = [tree]

    while stack:
        curr_node = stack.pop()
        if not curr_node.left or curr_node.left in visited:
            res.append(curr_node.data)
            if curr_node.right:
                stack.append(curr_node.right)
        else:
            stack.append(curr_node)
            if curr_node.left:
                stack.append(curr_node.left)

        visited.add(curr_node)

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
