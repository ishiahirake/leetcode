import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = sorted(nums, reverse=True)[:k]
        heapq.heapify(self.pq)

    def add(self, val: int) -> int:
        if len(self.pq) >= self.k:
            if self.pq[0] < val:
                heapq.heappushpop(self.pq, val)
        else:
            heapq.heappush(self.pq, val)
        return self.pq[0]
