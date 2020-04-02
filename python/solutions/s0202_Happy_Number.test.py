import unittest

from s0202_Happy_Number import Solution

s = Solution()


class MyTestCase(unittest.TestCase):

    def test_n(self):
        self.assertFalse(0)
        self.assertTrue(1)
        self.assertTrue(s.isHappy(19))


if __name__ == '__main__':
    unittest.main()
