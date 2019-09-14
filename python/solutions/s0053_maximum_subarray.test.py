import unittest

from s0053_maximum_subarray import Solution

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(6, solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == '__main__':
    unittest.main()
