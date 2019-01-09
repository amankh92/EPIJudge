from test_framework import generic_test


def remove_duplicates(L):
    head = uniq = it = L
    while it:
        next_num = it.next
        if next_num and next_num.data == it.data:
            pass
        else:
            uniq.next = next_num
            uniq = uniq.next
        it = it.next
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
