from test_framework import generic_test


def is_symmetric(tree):
    def check(root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and root2:
            return root1.data == root2.data and check(root1.left, root2.right) and check(root1.right, root2.left)
        return False
    # TODO - you fill in here.
    return not tree or check(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
