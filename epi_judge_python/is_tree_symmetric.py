from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque

def is_symmetric(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True
    
    queue = deque([tree])

    while queue:
        l = 0
        r = len(queue)-1
        while l<=r:
            left = queue[l].data if queue[l] else None
            right = queue[r].data if queue[r] else None
            if left != right:
                return False
            l += 1
            r -= 1

        curr_len = len(queue)
        for _ in range(curr_len):
            curr_node = queue.popleft()
            if curr_node:
                queue.extend([curr_node.left, curr_node.right])

    return True
        

        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
