import unittest

from s0231_Power_of_Two import Solution


class MyTestCase(unittest.TestCase):

    def test_n(self):
        s = Solution()

        self.assertTrue(s.isPowerOfTwo(1))
        self.assertTrue(s.isPowerOfTwo(16))

        self.assertFalse(s.isPowerOfTwo(218))
        self.assertFalse(s.isPowerOfTwo(0))


if __name__ == '__main__':
    unittest.main()
