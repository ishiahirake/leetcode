from collections import deque
from typing import List


class Solution:
    """
    239. Sliding Window Maximum.

    :see https://leetcode.com/problems/sliding-window-maximum/
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        window, res = deque(), []
        for i, v in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.popleft()
            while window and nums[window[-1]] <= v:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res
