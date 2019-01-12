import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree):

    lbl = []
    rbl = []

    def is_leaf(node):
        return not node.left and not node.right

    def left(node, is_boundary):
        # pre-order because nodes are to be appended to result while going down
        if node is None:
            return None

        if is_boundary or is_leaf(node):
            lbl.append(node)

        left(node.left, is_boundary)
        left(node.right, is_boundary and not node.left)

    def right(node, is_boundary):
        # post-order because nodes are to be appended to result while going up
        if node is None:
            return None

        right(node.left, is_boundary and not node.right)
        right(node.right, is_boundary)

        if is_boundary or is_leaf(node):
            rbl.append(node)

    if tree is not None:
        left(tree.left, True)
        right(tree.right, True)
    # TODO - you fill in here.
    return ([tree] + lbl + rbl) if tree else []


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
                                       create_output_list_wrapper))
