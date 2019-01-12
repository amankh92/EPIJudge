from test_framework import generic_test
from binary_tree_node import BinaryTreeNode


def binary_tree_from_preorder_inorder(preorder, inorder):
    lookup = {data: i for i, data in enumerate(inorder)}

    def helper(pre_s, pre_e, in_s, in_e):
        if pre_s > pre_e or in_s > in_e:
            return None
        node_id_inorder = lookup[preorder[pre_s]]
        left_size = node_id_inorder - in_s
        return BinaryTreeNode(preorder[pre_s], helper(pre_s + 1, pre_s + left_size, in_s, node_id_inorder - 1),
                                               helper(pre_s + 1 + left_size, pre_e, node_id_inorder + 1, in_e))
    # TODO - you fill in here.
    return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
