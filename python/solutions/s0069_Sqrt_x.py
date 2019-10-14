class Solution:
    """
    69. Sqrt(x).

    :see https://leetcode.com/problems/sqrtx/
    """

    def mySqrt(self, x: int) -> int:
        li, hi = 0, x // 2 + 1
        while li <= hi:
            mid = (li + hi) // 2
            mid_pow_2 = mid ** 2
            if mid_pow_2 <= x:
                if (mid + 1) ** 2 > x:
                    return mid
                else:
                    li = mid + 1
            else:
                hi = mid - 1
        return x
