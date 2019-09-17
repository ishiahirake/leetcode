class Solution:

    def myPow(self, x: float, n: int) -> float:
        x = x if n > 0 else 1 / x
        memo = {0: 1, 1: x}

        def f(s: int) -> float:
            if s in memo:
                return memo[s]
            memo[s] = f(s // 2) * f((s + 1) // 2)
            return memo[s]

        return f(abs(n))
