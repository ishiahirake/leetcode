import unittest

from lib import TreeNode
from s0111_Minimum_Depth_of_Binary_Tree import Solution

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

        self.assertEqual(2, s.minDepth(n3))


if __name__ == '__main__':
    unittest.main()
