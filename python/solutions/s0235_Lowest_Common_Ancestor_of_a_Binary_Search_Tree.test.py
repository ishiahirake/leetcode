import unittest

from lib import TreeNode
from s0235_Lowest_Common_Ancestor_of_a_Binary_Search_Tree import Solution

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        n0 = TreeNode(0)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n6 = TreeNode(6)
        n7 = TreeNode(7)
        n8 = TreeNode(8)
        n9 = TreeNode(9)

        n4.left = n3
        n4.right = n5
        n2.left = n0
        n2.right = n4
        n8.left = n7
        n8.right = n9
        n6.left = n2
        n6.right = n8

        self.assertEqual(6, solution.lowestCommonAncestor(n6, n2, n8).val)
        self.assertEqual(2, solution.lowestCommonAncestor(n6, n2, n4).val)

    def test_e1(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)

        n2.left = n1

        self.assertEqual(2, solution.lowestCommonAncestor(n2, n2, n1).val)


if __name__ == '__main__':
    unittest.main()
