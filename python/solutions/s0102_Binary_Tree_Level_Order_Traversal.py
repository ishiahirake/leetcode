from typing import List

from lib import TreeNode


class Solution:
    """
    102. Binary Tree Level Order Traversal

    :see https://leetcode.com/problems/binary-tree-level-order-traversal/
    """

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        orders, nodes = [], [root]
        while nodes:
            orders.append([])
            children = []
            for node in nodes:
                orders[-1].append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            nodes = children
        return orders
