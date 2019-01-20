from test_framework import generic_test
from binary_tree_node import BinaryTreeNode


def rebuild_bst_from_preorder(preorder_sequence):
    def rebuild(low_limit, upper_limit):
        if root_ids[0] == len(preorder_sequence):
            return None
        root = preorder_sequence[root_ids[0]]
        if not low_limit <= root <= upper_limit:
            return None
        root_ids[0] += 1
        left_subtree = rebuild(low_limit, root)
        right_subtree = rebuild(root, upper_limit)
        return BinaryTreeNode(root, left_subtree, right_subtree)

    root_ids = [0]
    return rebuild(float('-inf'), float('inf'))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
