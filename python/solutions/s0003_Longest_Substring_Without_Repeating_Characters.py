class Solution:
    """
    3. Longest Substring Without Repeating Characters

    :see https://leetcode.com/problems/longest-substring-without-repeating-characters/
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = li = 0
        char_indexes = {}
        for hi, char in enumerate(s):
            ei = char_indexes.get(char)
            if ei is not None and ei >= li:
                li = char_indexes.get(char) + 1
            char_indexes[char] = hi
            max_len = max(max_len, hi - li + 1)
        return max_len
