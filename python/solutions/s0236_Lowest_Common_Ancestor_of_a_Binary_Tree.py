from lib import TreeNode


class Solution:
    """
    236. Lowest Common Ancestor of a Binary Tree.

    :see https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
    """

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        return left if right is None else right
