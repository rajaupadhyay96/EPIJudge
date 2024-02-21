import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# def lca(node0: BinaryTreeNode,
#         node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
#     nodes_seen = set([node0])

#     while node0:
#         node0 = node0.parent
#         nodes_seen.add(node0)
    
#     while node1:
#         if node1 in nodes_seen:
#             return node1
#         node1 = node1.parent

#     return None

def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    len_0 = 0
    len_1 = 0

    node0_tmp = node0
    node1_tmp = node1

    while node0_tmp:
        len_0 += 1
        node0_tmp = node0_tmp.parent

    while node1_tmp:
        len_1 += 1
        node1_tmp = node1_tmp.parent

    if len_0 > len_1:
        diff = len_0 - len_1

        while diff > 0:
            node0 = node0.parent
            diff -= 1

    if len_1 > len_0:
        diff = len_1 - len_0
        while diff > 0:
            node1 = node1.parent
            diff -= 1

    while node0 and node1 and node0 != node1:
        node1 = node1.parent
        node0 = node0.parent

    return node0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
