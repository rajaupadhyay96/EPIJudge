from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if not L:
        return None
    
    if start == finish:
        return L
    
    l = 1
    l_ptr = L

    l_prev_head = ListNode(None, L)
    res = l_prev_head
    while l != start:
        l_prev_head = l_ptr
        l_ptr = l_ptr.next
        l += 1

    r = 1
    r_ptr = L
    
    while r != finish:
        r_ptr = r_ptr.next
        r += 1
    
    r_next_tail = r_ptr.next

    l_prev = l_ptr
    curr_node = l_ptr.next
    while curr_node != r_next_tail:
        next_node = curr_node.next
        curr_node.next = l_prev
        l_prev = curr_node
        curr_node = next_node

    l_prev_node = l_prev_head.next
    l_prev_node.next = curr_node
    l_prev_head.next = l_prev

    return res.next


    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
