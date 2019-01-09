from test_framework import generic_test


def is_linked_list_a_palindrome(L):
    def reverse(start):
        prev = None
        cur = start
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    slow = fast = L
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    first_iter = L
    second_iter = reverse(slow)
    while first_iter and second_iter:
        if first_iter.data != second_iter.data:
            return False
        first_iter = first_iter.next
        second_iter = second_iter.next
    # TODO - you fill in here.
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
