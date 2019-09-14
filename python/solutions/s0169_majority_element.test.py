import unittest

from s0169_majority_element import Solution

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(3, solution.majorityElement([3, 2, 3]))
        self.assertEqual(2, solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))


if __name__ == '__main__':
    unittest.main()
