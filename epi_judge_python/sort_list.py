from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# Bubble sort
# def stable_sort_list(L: ListNode) -> Optional[ListNode]:
#     n = 0
#     l_ptr = L
#     while l_ptr:
#         n += 1
#         l_ptr = l_ptr.next

#     for i in range(n):
#         l_ptr = L
#         for j in range(n-i-1):
#             if l_ptr.data > l_ptr.next.data:
#                 l_ptr.data, l_ptr.next.data = l_ptr.next.data, l_ptr.data
#             l_ptr = l_ptr.next

#     return L    

def merge(l, r):
    res = ListNode(0)
    res_ptr = res

    l_ptr = l
    r_ptr = r

    while l_ptr and r_ptr:
        if l_ptr.data - r_ptr.data < 0:
            new_node = ListNode(l_ptr.data)
            l_ptr = l_ptr.next
        else:
            new_node = ListNode(r_ptr.data)
            r_ptr = r_ptr.next
        res_ptr.next = new_node
        res_ptr = res_ptr.next

    while l_ptr:
        new_node = ListNode(l_ptr.data)
        l_ptr = l_ptr.next
        res_ptr.next = new_node
        res_ptr = res_ptr.next

    while r_ptr:
        new_node = ListNode(r_ptr.data)
        r_ptr = r_ptr.next
        res_ptr.next = new_node
        res_ptr = res_ptr.next

    return res.next

    

def merge_sort(lst):
    if lst is None or lst.next is None:
        return lst
    
    left_ptr = lst
    slow = lst
    fast = lst
    prev = lst
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    right_ptr = prev.next
    prev.next = None

    l = merge_sort(left_ptr)
    r = merge_sort(right_ptr)
    res = merge(l, r)
    return res


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    return merge_sort(L)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
