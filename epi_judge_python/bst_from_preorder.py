from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    
    def _build(l, r):
        if l == r:
            return BstNode(preorder_sequence[l])
        if l > r:
            return None
        
        node = BstNode(preorder_sequence[l])

        ptr = l+1
        while ptr <= r and preorder_sequence[ptr] < node.data:
            ptr += 1

        node.left = _build(l+1, ptr-1)
        node.right = _build(ptr, r)

        return node
    
    return _build(0, len(preorder_sequence)-1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
