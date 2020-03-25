class Solution:
    """
    191. Number of 1 Bits.

    :see https://leetcode.com/problems/number-of-1-bits/
    """

    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n != 0:
            weight += 1
            n &= n - 1
        return weight
