from lib import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    450. Delete Node in a BST.

    :see https://leetcode.com/problems/delete-node-in-a-bst/
    """

    # noinspection PyPep8Naming
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is not None and root.right is None:
                return root.left
            elif root.left is None and root.right is not None:
                return root.right
            else:
                node, parent = self._find_min_node_parent(root.right, None)
                if parent:
                    parent.left = node.right
                node.left = root.left
                if root.right is not node:
                    node.right = root.right
                return node

    @staticmethod
    def _find_min_node_parent(node: TreeNode, parent):
        while node.left:
            parent = node
            node = node.left
        return node, parent
