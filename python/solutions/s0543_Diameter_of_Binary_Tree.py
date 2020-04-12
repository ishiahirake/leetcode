from lib import TreeNode


class Solution:
    """
    543. Diameter of Binary Tree.

    :see https://leetcode.com/problems/diameter-of-binary-tree/
    """

    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.diameter

    def depth(self, node: TreeNode):
        if not node:
            return 0
        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        self.diameter = max(self.diameter, left_depth + right_depth)
        return max(left_depth, right_depth) + 1
