from typing import List


class Solution:
    """
    136. Single Number.

    :see https://leetcode.com/problems/single-number/
    """

    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return s.pop()
