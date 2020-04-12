from typing import List


class Solution:
    """
    1046. Last Stone Weight.

    :see https://leetcode.com/problems/last-stone-weight/
    """

    def lastStoneWeight(self, stones: List[int]) -> int:
        return self.smash(stones)

    def smash(self, stones: List[int]) -> int:
        if not stones:
            return 0
        elif len(stones) == 1:
            return stones[0]
        else:
            sorted_stones = sorted(stones, reverse=True)
            y = sorted_stones.pop(0)
            x = sorted_stones.pop(0)
            if x != y:
                sorted_stones.append(y - x)
            return self.smash(sorted_stones)
