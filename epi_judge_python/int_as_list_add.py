from test_framework import generic_test
from list_node import ListNode


def add_two_numbers(L1, L2):
    iter1 = L1
    iter2 = L2
    carry = 0
    dummy_head = new_iter = ListNode(0)
    while iter1 or iter2 or carry:
        sum = (iter1.data if iter1 else 0) + (iter2.data if iter2 else 0) + carry
        new_iter.next = ListNode(sum % 10)
        new_iter = new_iter.next
        carry = sum // 10
        iter1 = iter1.next if iter1 else None
        iter2 = iter2.next if iter2 else None
    # TODO - you fill in here.
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
