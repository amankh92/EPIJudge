from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    # TODO - you fill in here.
    result = []

    def reverse_inorder_traversal(tree):
        if not tree:
            return
        reverse_inorder_traversal(tree.right)
        if len(result) < k:
            result.append(tree.data)
        reverse_inorder_traversal(tree.left)

    reverse_inorder_traversal(tree)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
