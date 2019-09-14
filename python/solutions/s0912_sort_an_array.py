import random


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

        left, mid, right = [], [], []
        pivot = random.choice(nums)
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                right.append(num)

        return self.quick_sort(left) + mid + self.quick_sort(right)
