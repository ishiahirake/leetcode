from lib import TreeNode


class Solution:
    """
    98. Validate Binary Search Tree.

    :see https://leetcode.com/problems/validate-binary-search-tree/
    """

    def isValidBST(self, root: TreeNode) -> bool:
        last = None

        def inorder_validate(node: TreeNode):
            nonlocal last
            if not node:
                return True
            if not inorder_validate(node.left):
                return False
            if last and last.val >= node.val:
                return False
            last = node
            return inorder_validate(node.right)

        return inorder_validate(root)
