import unittest

from s0022_Generate_Parentheses import Solution

s = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(sorted([
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ]), sorted(s.generateParenthesis(3)))


if __name__ == '__main__':
    unittest.main()
