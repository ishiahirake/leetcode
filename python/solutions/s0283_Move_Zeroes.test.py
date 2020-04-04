import unittest

from s0283_Move_Zeroes import Solution

s = Solution()


class MyTestCase(unittest.TestCase):

    def test_n(self):
        nums = [0, 1, 0, 3, 12]
        s.moveZeroes(nums)
        self.assertEqual([1, 3, 12, 0, 0], nums)

    def test_e1(self):
        nums = [1]
        s.moveZeroes(nums)
        self.assertEqual([1], nums)


if __name__ == '__main__':
    unittest.main()
