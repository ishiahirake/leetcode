from typing import List


class Solution:
    """
    15. 3Sum.

    :see https://leetcode.com/problems/3sum/
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result, last = [], None
        for idx, target in enumerate(nums):
            # since result can't be duplicated,
            # so just ignore item which value equals to last one
            if target == last:
                continue
            last = target
            for two in self._two_sum(nums[idx + 1:], 0 - target):
                result.append([target] + two)

        return result

    @staticmethod
    def _two_sum(nums: List[int], target: int) -> List[List[int]]:
        li, hi = 0, len(nums) - 1
        while li < hi:
            num_sum = nums[li] + nums[hi]
            if num_sum == target:
                yield [nums[li], nums[hi]]
            # move to next li which value not equals to current one
            if num_sum <= target:
                while li < hi and nums[li] == nums[li + 1]:
                    li += 1
                li += 1
            # move to next hi which value not equals to current one
            if num_sum >= target:
                while hi > li and nums[hi] == nums[hi - 1]:
                    hi -= 1
                hi -= 1
