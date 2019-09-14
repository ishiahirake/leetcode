
brackets = {
    '}': '{',
    ')': '(',
    ']': '[',
}


class Solution:
    """
    20. Valid Parentheses.

    :see https://leetcode.com/problems/valid-parentheses/.
    """

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in brackets.values():
                stack.append(c)
            elif not stack or brackets[c] != stack.pop():
                return False
        return not stack
