from test_framework import generic_test


def find_first_greater_than_k(tree, k):
    # TODO - you fill in here.
    value = 0
    while tree:
        if tree.data > k:
            value = tree
            tree = tree.left
        else:
            tree = tree.right
    return value


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
