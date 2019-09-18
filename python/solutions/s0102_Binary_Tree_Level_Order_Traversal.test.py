import unittest

from lib import TreeNode
from s0102_Binary_Tree_Level_Order_Traversal import Solution

s = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        n3 = TreeNode(3)
        n9 = TreeNode(9)
        n20 = TreeNode(20)
        n15 = TreeNode(15)
        n7 = TreeNode(7)

        n20.left = n15
        n20.right = n7
        n3.left = n9
        n3.right = n20

        self.assertEqual([
            [3],
            [9, 20],
            [15, 7]
        ], s.levelOrder(n3))


if __name__ == '__main__':
    unittest.main()
