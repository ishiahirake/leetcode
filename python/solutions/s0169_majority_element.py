
class Solution:
    """
    169. Majority Element.

    :see https://leetcode.com/problems/majority-element/
    """

    def majorityElement(self, nums: list) -> int:
        elements = {}
        for num in nums:
            elements[num] = elements.get(num, 0) + 1
        return max(elements.keys(), key=elements.get)
