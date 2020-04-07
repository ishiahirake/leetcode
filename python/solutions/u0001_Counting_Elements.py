from collections import Counter
from typing import List


class Solution:
    """
    Counting Elements.

    :see https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/
    """

    def countElements(self, arr: List[int]) -> int:
        elements = Counter(arr)
        keys = sorted(elements.keys())

        count = 0
        for i in range(len(keys) - 1):
            if keys[i] + 1 == keys[i + 1]:
                count += elements[keys[i]]
        return count
