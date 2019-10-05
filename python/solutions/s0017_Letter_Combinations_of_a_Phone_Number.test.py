import unittest

from s0017_Letter_Combinations_of_a_Phone_Number import Solution

s = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(
            sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            sorted(s.letterCombinations("23"))
        )

    def test_e1(self):
        self.assertEqual(
            sorted([]),
            sorted(s.letterCombinations(""))
        )


if __name__ == '__main__':
    unittest.main()
