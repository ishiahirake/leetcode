class Solution:
    """
    932. Beautiful Array

    :see https://leetcode.com/problems/beautiful-array/
    """

    def beautifulArray(self, n: int) -> list:
        memo = {1: [1]}

        def f(num: int) -> list:
            if num not in memo:
                odds = f((num + 1) // 2)
                evens = f(num // 2)
                memo[num] = [i * 2 - 1 for i in odds] + [i * 2 for i in evens]
            return memo[num]

        return f(n)

