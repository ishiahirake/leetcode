import unittest

from s0050_Pow_x_n import Solution

s = Solution()


def is_equals(e, r) -> bool:
    return abs(e - r) < 0.0000000001


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(is_equals(1024.00000, s.myPow(2.00000, 10)))
        self.assertTrue(is_equals(9.26100, s.myPow(2.10000, 3)))
        self.assertTrue(is_equals(0.25000, s.myPow(2.00000, -2)))

    def test_e1(self):
        self.assertTrue(is_equals(1, s.myPow(0.44528, 0)))


if __name__ == '__main__':
    unittest.main()
