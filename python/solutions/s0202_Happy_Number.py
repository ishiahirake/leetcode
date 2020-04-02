def digits_sum(num: int) -> int:
    return sum([int(n) ** 2 for n in str(num)])


class Solution:
    """
    202. Happy Number.

    :see https://leetcode.com/problems/happy-number/
    """

    def isHappy(self, n: int) -> bool:
        nums = set()
        while n not in nums:
            if n == 1:
                return True
            nums.add(n)
            n = digits_sum(n)

        return False
