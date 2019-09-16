from typing import List


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


def _gen_n_sum(func):
    def n_sum(nums: List[int], target: int):
        result, last = [], None
        for idx, val in enumerate(nums):
            # since result can't be duplicated,
            # so just ignore item which value equals to last one
            if val == last:
                continue
            last = val
            for two in func(nums[idx + 1:], target - val):
                result.append([val] + two)

        return result

    return n_sum


def make_n_sum(n):
    func = _two_sum
    for i in range(2, n):
        func = _gen_n_sum(func)

    def f(nums: List[int], target: int):
        return func(sorted(nums), target)

    return f


four_sum = make_n_sum(4)


class Solution:
    """
    18. 4Sum.

    :see https://leetcode.com/problems/4sum/
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return four_sum(nums, target)
