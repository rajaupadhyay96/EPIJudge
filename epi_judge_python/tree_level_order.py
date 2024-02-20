from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    res = []

    stack = deque([tree])

    while stack:
        curr_len = len(stack)
        tmp = []
        for _ in range(curr_len):
            node = stack.popleft()
            if node:
                tmp.append(node.data)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        if tmp:
            res.append(tmp)

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
