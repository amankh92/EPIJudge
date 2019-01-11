from test_framework import generic_test

# [-4, -3, -5, -9, 4, 2, 2, 1, 8, -4, -6, -2, -6, -5, 10, -2, 10, -3, 10, 5, 9, 6, 1, -4, -1, 10, -8, 3, -11, -4, -12]

def inorder_traversal(tree):
    result = []

    def helper(node):
        if node is None:
            return
        helper(node.left)
        result.append(node.data)
        helper(node.right)
    helper(tree)
    return result


def inorder_traversl(tree):
    stack = []
    result = []
    while tree or stack:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            popped = stack.pop()
            result.append(popped.data)
            tree = popped.right
    print(result)
    return result

def inorder_traversal1(tree):
    stack = []
    result = []
    while tree or len(stack) > 0:
        if tree is None:
            popped = stack.pop()
            result.append(popped.data)
            tree = popped.right
        elif tree.left:
            stack.append(tree)
            tree = tree.left
        else:
            result.append(tree.data)
            if tree.right:
                tree = tree.right
            else:
                if tree.right is None and len(stack) == 0:
                    break
                popped = stack.pop()
                result.append(popped.data)
                tree = popped.right
    # TODO - you fill in here.
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
