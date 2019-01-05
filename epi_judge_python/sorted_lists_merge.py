from test_framework import generic_test


def merge_two_sorted_lists(L1, L2):
    head = None
    tail = head
    while L1 and L2:
        if L1.data <= L2.data:
            if head is None:
                head = L1
                tail = head
            else:
                tail.next = L1
                tail = tail.next
            L1 = L1.next
        else:
            if head is None:
                head = L2
                tail = head
            else:
                tail.next = L2
                tail = tail.next
            L2 = L2.next
    if head is None:
        head = L1 or L2
        # tail = head
    else:
        tail.next = L1 or L2
    # TODO - you fill in here.
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
