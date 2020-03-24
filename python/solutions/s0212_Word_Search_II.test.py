import unittest

from s0212_Word_Search_II import Solution


class MyTestCase(unittest.TestCase):

    def test_n1(self):
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ]
        words = ["oath", "pea", "eat", "rain"]
        self.assert_find_words(board, words, ["eat","oath"])

    def test_e1(self):
        self.assert_find_words(
            board=[["a","a"]],
            words=["a"],
            excepted=["a"]
        )

    def assert_find_words(self, board, words, excepted):
        s = Solution()
        self.assertEqual(sorted(excepted), sorted(s.findWords(board, words)))


if __name__ == '__main__':
    unittest.main()
