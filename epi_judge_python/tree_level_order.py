from test_framework import generic_test
from collections import deque


def binary_tree_depth_order(tree):
    if not tree:
        return []
    result = []
    queue = []
    queue.append(tree)
    # result.append([tree.data])
    while queue:
        result.append([node.data for node in queue])
        queue = [node for tnode in queue for node in [tnode.left, tnode.right] if node]
        # queue.pop(0)
        # result.append([tnode.data for tnode in queue])
    # TODO - you fill in here.
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
