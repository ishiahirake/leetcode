from collections import Counter


class Solution:
    """
    3. Longest Substring Without Repeating Characters

    :see https://leetcode.com/problems/longest-substring-without-repeating-characters/
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = li = 0
        counter = Counter()
        for hi, char in enumerate(s):
            counter[char] += 1
            while len(counter) != (hi - li + 1):
                old_char = s[li]
                counter[old_char] -= 1
                if counter[old_char] == 0:
                    del counter[old_char]
                li += 1
            max_len = max(max_len, len(counter))
        return max_len
