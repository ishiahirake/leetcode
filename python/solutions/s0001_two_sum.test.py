import unittest

from s0001_two_sum import Solution

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual([0, 1], sorted(solution.twoSum([2, 7, 11, 15], 9)))


if __name__ == '__main__':
    unittest.main()
