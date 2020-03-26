from typing import List


class Solution:
    """
    338. Counting Bits.

    :see https://leetcode.com/problems/counting-bits/
    """

    def countBits(self, num: int) -> List[int]:
        if num < 0:
            return []
        bits = [0]
        for i in range(1, num + 1):
            bits.append(bits[i & (i - 1)] + 1)
        return bits
