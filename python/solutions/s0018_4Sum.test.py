import unittest
from typing import List

from s0018_4Sum import Solution, make_n_sum


def ssr(nums: List[List[int]]) -> List[List[int]]:
    nums = list(map(sorted, nums))
    return sorted(nums)


solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(ssr([
            [-1, 0, 0, 1],
            [-2, -1, 1, 2],
            [-2, 0, 0, 2]
        ]), ssr(solution.fourSum([1, 0, -1, 0, -2, 2], 0)))

    def test_5_sum(self):
        five_sum = make_n_sum(5)
        self.assertEqual(ssr([
            [-2, -1, 0, 1, 2],
            [-2, 0, 0, 0, 2],
            [-1, 0, 0, 0, 1],
        ]), ssr(five_sum([1, 0, -1, 0, -2, 2, 0], 0)))


if __name__ == '__main__':
    unittest.main()
