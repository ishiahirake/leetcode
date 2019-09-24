class Solution:
    """
    22. Generate Parentheses.

    :see https://leetcode.com/problems/generate-parentheses/
    """

    def generateParenthesis(self, n):
        ans = []

        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack()
        return ans
