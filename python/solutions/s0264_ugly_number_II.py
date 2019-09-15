import heapq
from typing import List


class Ugly:

    def __init__(self, n: int) -> None:
        self.nums = self.make_ugly(n)

    @staticmethod
    def make_ugly(n: int) -> List[int]:
        nums, heap, saw = [], [1], []

        for _ in range(n):
            num = heapq.heappop(heap)
            nums.append(num)
            for factor in [2, 3, 5]:
                ugly = factor * num
                if ugly not in saw:
                    heapq.heappush(heap, ugly)
                    saw.append(ugly)

        return nums


class Solution:
    ugly = Ugly(1690)

    def nthUglyNumber(self, n: int) -> int:
        return self.ugly.nums[n - 1]
