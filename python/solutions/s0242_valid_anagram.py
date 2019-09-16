from collections import Counter


class Solution:
    """
    242. Valid Anagram.

    :see https://leetcode.com/problems/valid-anagram/
    """
    def isAnagram(self, s: str, t: str) -> bool:
        return False if len(s) != len(t) else Counter(s) == Counter(t)
