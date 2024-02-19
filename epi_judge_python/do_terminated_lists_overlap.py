import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    l0_len = 0
    l0_ptr = l0
    while l0_ptr:
        l0_len += 1
        l0_ptr = l0_ptr.next
    
    l1_len = 0
    l1_ptr = l1
    while l1_ptr:
        l1_len += 1
        l1_ptr = l1_ptr.next

    l0_ptr = l0
    l1_ptr = l1
    if l1_len > l0_len:
        diff = l1_len - l0_len
        while diff > 0:
            l1_ptr = l1_ptr.next
            diff -= 1

    if l0_len > l1_len:
        diff = l0_len - l1_len
        while diff > 0:
            l0_ptr = l0_ptr.next
            diff -= 1

    while l0_ptr and l1_ptr:
        if l0_ptr == l1_ptr:
            return l0_ptr
        l0_ptr = l0_ptr.next
        l1_ptr = l1_ptr.next

    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
