import unittest

from s0912_sort_an_array import Solution

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_sort(self):
        self.assertEqual([1, 2, 3, 5], solution.sortArray([5, 2, 3, 1]))
        self.assertEqual([0, 0, 1, 1, 2, 5], solution.sortArray([5, 1, 1, 2, 0, 0]))


if __name__ == '__main__':
    unittest.main()
