import unittest
from typing import List

from s0015_3Sum import Solution

solution = Solution()


def sort_solution_result(nums: List[List[int]]) -> List[List[int]]:
    nums = list(map(sorted, nums))
    return sorted(nums)


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(sort_solution_result(
            [
                [-1, 0, 1],
                [-1, -1, 2]
            ]
        ), sort_solution_result(solution.threeSum([-1, 0, 1, 2, -1, -4])))

    def test_e1(self):
        self.assertEqual([[0, 0, 0]],
                         sort_solution_result(solution.threeSum([0, 0, 0, 0])))

    def test_e2(self):
        self.assertEqual([[-1, 0, 1]],
                         sort_solution_result(solution.threeSum([1, -1, -1, 0])))


if __name__ == '__main__':
    unittest.main()
