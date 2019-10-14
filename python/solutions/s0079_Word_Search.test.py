import unittest

from s0079_Word_Search import Solution

s = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]

        self.assertTrue(s.exist(board, "ABCCED"))
        self.assertTrue(s.exist(board, "SEE"))
        self.assertFalse(s.exist(board, "ABCB"))

    def test_e1(self):
        board = [["a", "a"]]
        self.assertFalse(s.exist(board, "aaa"))

    def test_e2(self):
        board = [["a", "b"], ["c", "d"]]
        self.assertTrue(s.exist(board, "acdb"))


if __name__ == '__main__':
    unittest.main()
