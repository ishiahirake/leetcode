from typing import List


class Solution:
    """
    283. Move Zeroes.

    :see https://leetcode.com/problems/move-zeroes/
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        li = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != li:
                    nums[li] = nums[i]
                li += 1
        for i in range(li, len(nums)):
            nums[i] = 0
