from lib import TreeNode


class Solution:
    """
    111. Minimum Depth of Binary Tree.

    :see https://leetcode.com/problems/minimum-depth-of-binary-tree/
    """

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodes, level = [root], 1
        while True:
            children = []
            for node in nodes:
                if not node.left and not node.right:
                    return level
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            level += 1
            nodes = children
