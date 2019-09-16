from lib import TreeNode


class Solution:
    """
    235. Lowest Common Ancestor of a Binary Search Tree.

    :see https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
    """

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        le, gt = (p, q) if p.val < q.val else (q, p)

        def f(node: TreeNode) -> TreeNode:
            # For BST, LCA is the node which it's value between(p.val, q.val)
            if le.val <= node.val <= gt.val:
                return node
            return f(node.right) if node.val < le.val else f(node.left)

        return f(root)
