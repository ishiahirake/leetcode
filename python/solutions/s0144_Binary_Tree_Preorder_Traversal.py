from typing import List

from lib import TreeNode


class Solution:
    """
    144. Binary Tree Preorder Traversal.

    :see https://leetcode.com/problems/binary-tree-preorder-traversal/
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self._preorder(root, [])

    def _preorder(self, root: TreeNode, values: list):
        if not root:
            return []

        values.append(root.val)
        self._preorder(root.left, values)
        self._preorder(root.right, values)

        return values
