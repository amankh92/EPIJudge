from test_framework import generic_test
import collections


def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    def checktree(node):
        if not node:
            return BalancedStatusWithHeight(True, -1)

        left_nodes = checktree(node.left)
        if not left_nodes.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_nodes = checktree(node.right)
        if not right_nodes.balanced:
            return BalancedStatusWithHeight(False, 0)
        is_balanced = (abs(left_nodes.height - right_nodes.height) <= 1)
        height = max(left_nodes.height, right_nodes.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)
    # TODO - you fill in here.
    return checktree(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
