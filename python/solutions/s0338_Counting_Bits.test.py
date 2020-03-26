import unittest

from s0338_Counting_Bits import Solution


class MyTestCase(unittest.TestCase):

    def test_n(self):
        s = Solution()

        self.assertEqual([0, 1, 1], s.countBits(2))
        self.assertEqual([0, 1, 1, 2, 1, 2], s.countBits(5))


if __name__ == '__main__':
    unittest.main()
