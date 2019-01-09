import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    def length(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    length0 = length(l0)
    length1 = length(l1)
    root0 = l0
    root1 = l1
    if length1 > length0:
        l0, l1 = l1, l0
        root0, root1 = root1, root0
    for _ in range(abs(length1 - length0)):
        l0 = l0.next
    while l0 and l1 and l0 is not l1:
        l0 = l0.next
        l1 = l1.next
    # TODO - you fill in here.
    return l0


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

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
