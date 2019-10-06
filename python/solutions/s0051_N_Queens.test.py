import unittest

from s0051_N_Queens import Solution

s = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual([
            [".Q..",
             "...Q",
             "Q...",
             "..Q."],
            ["..Q.",
             "Q...",
             "...Q",
             ".Q.."]
        ], s.solveNQueens(4))

    def test_s1(self):
        self.assertEqual([["Q"]], s.solveNQueens(1))
        self.assertEqual([], s.solveNQueens(2))
        self.assertEqual([], s.solveNQueens(3))


if __name__ == '__main__':
    unittest.main()
