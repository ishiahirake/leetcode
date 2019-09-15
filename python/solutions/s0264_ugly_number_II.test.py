import unittest

from s0264_ugly_number_II import Solution


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        solution = Solution()
        self.assertEqual(1, solution.nthUglyNumber(1))
        self.assertEqual(3, solution.nthUglyNumber(3))
        self.assertEqual(12, solution.nthUglyNumber(10))


if __name__ == '__main__':
    unittest.main()
