from test_framework import generic_test


def inorder_traversal(tree):
    result = []
    prev = None
    while tree:
        if prev is tree.right and tree.right:
            prev = tree
            tree = tree.parent
        elif tree.left and tree.left is not prev:
            prev = tree
            tree = tree.left
        else:
            result.append(tree.data)
            prev = tree
            if tree.right:
                tree = tree.right
            else:
                tree = tree.parent
    return result


def inorder_traversa(tree):
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
