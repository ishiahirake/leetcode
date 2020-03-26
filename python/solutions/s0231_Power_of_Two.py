class Solution:
    """
    231. Power of Two.

    :see https://leetcode.com/problems/power-of-two/
    """

    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0
