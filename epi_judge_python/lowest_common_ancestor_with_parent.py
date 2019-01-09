import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    def depth(node):
        count = 0
        while node:
            count += 1
            node = node.parent
        return count

    depth0 = depth(node0)
    depth1 = depth(node1)

    if depth0 < depth1:
        node0, node1 = node1, node0

    for _ in range(abs(depth1 - depth0)):
        node0 = node0.parent

    while node0 and node1:
        if node0.data == node1.data:
            return node0
        if node0.parent:
            node0 = node0.parent
        else:
            return node0
        if node1.parent:
            node1 = node1.parent
        else:
            return node1
    # TODO - you fill in here.
    return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
