import unittest

from u0001_Counting_Elements import Solution

s = Solution()


class MyTestCase(unittest.TestCase):

    def test_n(self):
        self.assertEqual(2, s.countElements([1, 2, 3]))
        self.assertEqual(0, s.countElements([1, 1, 3, 3, 5, 5, 7, 7]))
        self.assertEqual(3, s.countElements([1, 3, 2, 3, 5, 0]))
        self.assertEqual(2, s.countElements([1, 1, 2, 2]))


if __name__ == '__main__':
    unittest.main()
