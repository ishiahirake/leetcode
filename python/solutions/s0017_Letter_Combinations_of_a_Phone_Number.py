from typing import List

_digit_letters = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

class Solution:
    """
    17. Letter Combinations of a Phone Number.

    :see https://leetcode.com/problems/letter-combinations-of-a-phone-number/
    """

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letters = []
        def backtrace(digit='', s=''):
            if len(digit) == 0:
                letters.append(s)
                return
            chars = _digit_letters[digit[0]]
            for char in chars:
                backtrace(digit[1:], s + char)

        backtrace(digits)
        return letters
