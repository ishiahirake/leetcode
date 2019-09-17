import unittest

from s0122_Best_Time_to_Buy_and_Sell_Stock_II import Solution

s = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(7, s.maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(4, s.maxProfit([1, 2, 3, 4, 5]))
        self.assertEqual(0, s.maxProfit([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()
