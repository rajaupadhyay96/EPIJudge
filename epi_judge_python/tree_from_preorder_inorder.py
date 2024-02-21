from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    
    if len(preorder) != len(inorder):
        return None
    
    if len(preorder) == 1:
        return BinaryTreeNode(preorder[0])
    
    idx_map = {v: idx for idx, v in enumerate(inorder)}

    def _build_tree(p_l, p_r, i_l, i_r):
        if p_l >= p_r:
            return None
        
        node = BinaryTreeNode(preorder[p_l])
                
        if i_l == i_r:
            return node

        inorder_idx = idx_map[node.data]
        number_of_left_nodes = inorder_idx - i_l
        node.left = _build_tree(p_l+1, p_l+1+number_of_left_nodes, i_l, inorder_idx-1)
        number_of_right_nodes = i_r - inorder_idx
        node.right = _build_tree(p_l+1+number_of_left_nodes, p_l+number_of_left_nodes+number_of_right_nodes+1, inorder_idx+1, i_r)

        return node
    
    return _build_tree(0, len(preorder)-1, 0, len(inorder)-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
