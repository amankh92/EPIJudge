import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import collections


def lca(tree, node0, node1):
    Status = collections.namedtuple('Status', ('num_nodes', 'ancestor'))

    def lca_helper(node):
        if not node:
            return Status(0, None)
        left_result = lca_helper(node.left)
        if left_result.num_nodes == 2:
            return left_result

        right_result = lca_helper(node.right)
        if right_result.num_nodes == 2:
            return right_result

        num_nodes = left_result.num_nodes + right_result.num_nodes + (node0, node1).count(node)
        return Status(num_nodes, node if num_nodes == 2 else None)
    # TODO - you fill in here.
    return lca_helper(tree).ancestor


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
