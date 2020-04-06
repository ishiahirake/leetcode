from typing import List


def anagram_key(s: str) -> str:
    return ''.join(sorted(s))


class Solution:
    """
    49. Group Anagrams.

    :see https://leetcode.com/problems/group-anagrams/
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            anagrams.setdefault(anagram_key(s), []).append(s)
        return list(anagrams.values())
