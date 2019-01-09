from test_framework import generic_test


def cyclically_right_shift_list(L, k):
    if L is None:
        return L
    head = tail = L
    count = 1
    while tail.next:
        tail = tail.next
        count += 1
    length = count
    k %= count
    if k == 0:
        return L
    tail.next = head
    steps = length - k
    while steps:
        head = head.next
        tail = tail.next
        steps -= 1
    tail.next = None
    # TODO - you fill in here.
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
