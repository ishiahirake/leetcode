import unittest

from s0020_valid_parentheses import Solution

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(solution.isValid('()'))
        self.assertTrue(solution.isValid('()[]{}'))
        self.assertFalse(solution.isValid('(]'))
        self.assertFalse(solution.isValid('([)]'))
        self.assertTrue(solution.isValid('{[]}'))
        self.assertFalse(solution.isValid("["))


if __name__ == '__main__':
    unittest.main()
