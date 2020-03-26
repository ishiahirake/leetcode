from typing import List


class Solution:
    """
    338. Counting Bits.

    :see https://leetcode.com/problems/counting-bits/
    """

    def countBits(self, num: int) -> List[int]:
        bits = [0]
        last_power_of_two = 0
        for i in range(1, num + 1):
            if self.isPowerOfTwo(i):
                bits.append(1)
                last_power_of_two = i
            else:
                bits.append(1 + bits[i - last_power_of_two])
        return bits

    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0
