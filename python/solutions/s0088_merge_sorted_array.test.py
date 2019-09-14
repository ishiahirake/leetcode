import unittest

from s0088_merge_sorted_array import Solution

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        num1 = [1, 2, 3, 0, 0, 0]
        solution.merge(num1, 3, [2, 5, 6], 3)
        self.assertEqual([1, 2, 2, 3, 5, 6], num1)

    def test_n2_gt_0(self):
        num1 = [11, 12, 13, 0, 0, 0]
        solution.merge(num1, 3, [2, 5, 6], 3)
        self.assertEqual([2, 5, 6, 11, 12, 13], num1)


if __name__ == '__main__':
    unittest.main()
