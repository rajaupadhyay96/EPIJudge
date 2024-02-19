from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    l = L
    r = L
    dummy_node = ListNode(None, L)

    for _ in range(k):
        r = r.next

    prev = dummy_node
    while r:
        prev = l
        l = l.next
        r = r.next

    prev.next = l.next
    return dummy_node.next




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
