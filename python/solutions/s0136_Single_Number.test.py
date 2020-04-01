import unittest

from s0136_Single_Number import Solution

s = Solution()


class MyTestCase(unittest.TestCase):
    def test_n(self):
        self.assertEqual(1, s.singleNumber([2, 2, 1]))
        self.assertEqual(4, s.singleNumber([4, 1, 2, 1, 2]))


if __name__ == '__main__':
    unittest.main()
