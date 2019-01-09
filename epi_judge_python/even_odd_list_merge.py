from test_framework import generic_test
from list_node import ListNode


def even_odd_merge(L):
    # TODO - you fill in here.
    odd_head = ListNode(0)
    even_head = ListNode(0)
    lists = [even_head, odd_head]
    turns = 0
    while L:
        lists[turns].next = L
        lists[turns] = lists[turns].next
        L = L.next
        turns ^= 1
    lists[1].next = None
    lists[0].next = odd_head.next
    return even_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
