from test_framework import generic_test


def reverse_sublist(L, start, finish):
    def reverse(start):
        cur = start
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    if start == finish:
        return L
    revlist_tail = revlist_head = revlist_head_prev = revlist_tail_next = None
    cur = L
    i = 0
    while cur:
        i += 1
        if i < start:
            revlist_head_prev = cur
        if i == start:
            revlist_head = cur
        if i == finish:
            revlist_tail = cur
            revlist_tail_next = cur.next
        cur = cur.next
    revlist_tail.next = None
    revlist_tail = reverse(revlist_head)
    if revlist_head_prev:
        revlist_head_prev.next = revlist_tail
    else:
        L = revlist_tail
    revlist_head.next = revlist_tail_next
    # TODO - you fill in here.
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
