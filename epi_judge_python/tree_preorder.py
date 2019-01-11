from test_framework import generic_test


def preorder_traversal(tree):
    # TODO - you fill in here.
    result = []
    stack = []
    while tree or stack:
        if tree:
            stack.append(tree)
            result.append(tree.data)
            tree = tree.left
        else:
            popped = stack.pop()
            tree = popped.right
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
