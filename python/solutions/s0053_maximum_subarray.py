
class Solution:
    """
    53. Maximum Subarray.

    :see https://leetcode.com/problems/maximum-subarray/
    """

    def maxSubArray(self, nums: list) -> int:
        if not nums:
            return 0

        ret_max, sub_max = nums[0], nums[0]
        for i in range(1, len(nums)):
            sub_max = max(nums[i], nums[i] + sub_max)
            if sub_max > ret_max:
                ret_max = sub_max

        return ret_max
