from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return None
    
    even = L
    odd = L.next
    if not odd:
        return even
    
    odd_starter = odd
    while even and even.next and odd and odd.next:
        next_even = even.next.next
        even.next = next_even
        even = next_even

        next_odd = odd.next.next
        odd.next = next_odd
        odd = next_odd
        
    even.next = odd_starter
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
