from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    res = ListNode(None)
    head = res
    l1_ptr = L1
    l2_ptr = L2

    while l1_ptr and l2_ptr:
        if l1_ptr.data <= l2_ptr.data:
            new_node = ListNode(l1_ptr.data)
            res.next = new_node
            res = res.next
            l1_ptr = l1_ptr.next
        else:
            new_node = ListNode(l2_ptr.data)
            res.next = new_node
            res = res.next
            l2_ptr = l2_ptr.next

    while l1_ptr:
        new_node = ListNode(l1_ptr.data)
        res.next = new_node
        res = res.next
        l1_ptr = l1_ptr.next

    while l2_ptr:
        new_node = ListNode(l2_ptr.data)
        res.next = new_node
        res = res.next
        l2_ptr = l2_ptr.next

    return head.next
            


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
