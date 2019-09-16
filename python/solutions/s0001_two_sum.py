from typing import List


class Solution:
    """
    1. Two Sum.

    :see https://leetcode.com/problems/two-sum/
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(nums):
            opt_idx = d.get(target - num)
            if opt_idx is not None:
                return [idx, opt_idx]
            d[num] = idx
