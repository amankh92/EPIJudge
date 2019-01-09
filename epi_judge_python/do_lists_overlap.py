import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head):
    def len_cycle(node):
        count = 1
        cur = node.next
        while cur is not node:
            count += 1
            cur = cur.next
        return count
    if head is None:
        return None
    # TODO - you fill in here.
    slow = head
    fast = head.next
    p1 = p2 = head
    while fast and fast.next and fast.next.next:
        if slow is fast:
            for _ in range(len_cycle(slow)):
                p2 = p2.next
            while p1 and p2:
                if p1 is p2:
                    return p1
                p1 = p1.next
                p2 = p2.next
        slow = slow.next
        fast = fast.next.next
    return None


def stem_length(start, end):
    temp = start
    count = 0
    while temp is not end:
        count += 1
        temp = temp.next
    return count


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


def overlapping_lists(l0, l1):
    root0, root1 = has_cycle(l0), has_cycle(l1)
    if root0 is None and root1 is None:
        return overlapping_no_cycle_lists(l0, l1)
    if root0 is None and root1 or root1 is None and root0:
        return None
    temp = root0.next
    while temp and temp is not root0 and temp is not root1:
        temp = temp.next
    if temp is not root1:
        return None
    stem_length0, stem_length1 = stem_length(l0, root0), stem_length(l1, root1)
    if stem_length1 > stem_length0:
        l0, l1 = l1, l0
        root0, root1 = root1, root0
    for _ in range(abs(stem_length0 - stem_length1)):
        l0 = l0.next
    while l0 is not l1 and l0 is not root0 and l1 is not root1:
        l0 = l0.next
        l1 = l1.next
    return l0 if l0 is l1 else root0


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_lists_overlap.py",
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
