import unittest

from s0239_sliding_window_maximum import Solution

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual([3, 3, 5, 5, 6, 7],
                         solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

    def test_e1(self):
        self.assertEqual([], solution.maxSlidingWindow([], 0))

    def test_e2(self):
        self.assertEqual([1], solution.maxSlidingWindow([1], 1))

    def test_e3(self):
        self.assertEqual([1, -1], solution.maxSlidingWindow([1, -1], 1))

    def test_e4(self):
        self.assertEqual([7, 4], solution.maxSlidingWindow([7, 2, 4], 2))


if __name__ == '__main__':
    unittest.main()
