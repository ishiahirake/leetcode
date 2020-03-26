class Solution:
    """
    482. License Key Formatting.

    :see https://leetcode.com/problems/license-key-formatting/
    """

    def licenseKeyFormatting(self, S: str, K: int) -> str:
        keys = []
        index = 0
        for char in S[::-1]:
            if char == '-':
                continue
            keys.append(char.upper())
            index += 1
            if index % K == 0:
                keys.append('-')
        return ''.join(keys[::-1]).strip('-')
