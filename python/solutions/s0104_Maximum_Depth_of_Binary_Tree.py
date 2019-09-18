from lib import TreeNode


class Solution:
    """
    104. Maximum Depth of Binary Tree

    :see https://leetcode.com/problems/maximum-depth-of-binary-tree/
    """

    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, depth: int) -> int:
            if not node:
                return depth
            return max(dfs(node.left, depth), dfs(node.right, depth)) + 1

        return dfs(root, 0)
