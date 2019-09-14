
class Solution(object):

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.quick_sort(nums)

    def quick_sort(self, nums):
        if len(nums) < 2:
            return nums

        pivot = nums[0]

        le = [num for num in nums[1:] if num <= pivot]
        gt = [num for num in nums[1:] if num > pivot]

        return self.quick_sort(le) + [pivot] + self.quick_sort(gt)
