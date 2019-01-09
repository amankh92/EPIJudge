import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from list_node import ListNode


def list_pivoting(l, x):
    less_iter = less_head = ListNode(0)
    equal_iter = equal_head = ListNode(0)
    greater_iter = greater_head = ListNode(0)
    cur = l
    while cur:
        if cur.data < x:
            less_iter.next = cur
            less_iter = less_iter.next
        elif cur.data == x:
            equal_iter.next = cur
            equal_iter = equal_iter.next
        elif cur.data > x:
            greater_iter.next = cur
            greater_iter = greater_iter.next
        cur = cur.next
    greater_iter.next = None
    equal_iter.next = greater_head.next
    less_iter.next = equal_head.next
    # TODO - you fill in here.
    return less_head.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
