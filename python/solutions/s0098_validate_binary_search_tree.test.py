import unittest

from lib import TreeNode
from s0098_validate_binary_search_tree import Solution

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_e1(self):
        root = TreeNode(1)
        root.left = TreeNode(1)

        self.assertFalse(solution.isValidBST(root))


if __name__ == '__main__':
    unittest.main()
