import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.pq) >= self.k:
            if self.pq[0] < val:
                heapq.heappushpop(self.pq, val)
        else:
            heapq.heappush(self.pq, val)
        return self.pq[0]
