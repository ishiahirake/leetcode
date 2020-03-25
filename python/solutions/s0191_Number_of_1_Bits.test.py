import unittest

from s0191_Number_of_1_Bits import Solution


class MyTestCase(unittest.TestCase):

    def test_n(self):
        s = Solution()

        self.assertEqual(3, s.hammingWeight(0b00000000000000000000000000001011))
        self.assertEqual(1, s.hammingWeight(0b00000000000000000000000010000000))
        self.assertEqual(31, s.hammingWeight(0b11111111111111111111111111111101))

    def test_e1(self):
        s = Solution()

        self.assertEqual(1, s.hammingWeight(0b00010000000000000000000000000000))


if __name__ == '__main__':
    unittest.main()
