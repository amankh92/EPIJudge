from test_framework import generic_test


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    if tree is None:
        return True
    if tree.left is None and tree.right is None and low_range <= tree.data <= high_range:
        return True
    left_subtree = is_binary_tree_bst(tree.left, low_range, tree.data)
    right_subtree = is_binary_tree_bst(tree.right, tree.data, high_range)
    # TODO - you fill in here.
    return left_subtree and low_range <= tree.data <= high_range and right_subtree


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
