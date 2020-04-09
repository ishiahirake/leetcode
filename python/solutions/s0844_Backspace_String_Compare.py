def backspace_str(s: str) -> str:
    stack = []
    for char in s:
        if char == '#':
            if len(stack) != 0:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


class Solution:
    """
    844. Backspace String Compare.

    :see https://leetcode.com/problems/backspace-string-compare/
    """

    def backspaceCompare(self, S: str, T: str) -> bool:
        return backspace_str(S) == backspace_str(T)
