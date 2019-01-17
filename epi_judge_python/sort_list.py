from test_framework import generic_test
from list_node import ListNode


def stable_sort_list2(L):
    sorted = ListNode(0, L)

    while L and L.next:
        if L.data > L.next.data:
            pre = sorted
            target = L.next
            while pre.next.data < target.data:
                pre = pre.next
            temp = pre.next
            pre.next = target
            L.next = target.next
            target.next = temp
        else:
            L = L.next
    return sorted.next


def stable_sort_list(L):
    if L is None:
        return None
    sorted_list_head = None
    cur = L
    while cur:
        next_node = cur.next
        if sorted_list_head is None or sorted_list_head.data > cur.data:
            cur.next = sorted_list_head
            sorted_list_head = cur
        else:
            ref = sorted_list_head
            prev = None
            while ref and ref.data <= cur.data:
                prev = ref
                ref = ref.next
            cur.next = ref
            prev.next = cur
        cur = next_node
    # TODO - you fill in here.
    return sorted_list_head


def stable_sort_list1(L):
    if L is None:
        return None
    cur = L.next
    sorted_list_head = L
    sorted_list_head.next = None
    while cur:
        next_node = cur.next
        # cur.next = None
        if sorted_list_head.data > cur.data:
            cur.next = sorted_list_head
            sorted_list_head = cur
        else:
            ref = sorted_list_head
            prev = None
            while ref and ref.data <= cur.data:
                prev = ref
                ref = ref.next
            if ref is None:
                prev.next = cur
                prev.next.next = None
            else:
                cur.next = prev.next
                prev.next = cur
        cur = next_node
    # TODO - you fill in here.
    return sorted_list_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
