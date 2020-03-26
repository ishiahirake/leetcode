class Solution:
    """
    52. N-Queens II.

    :see https://leetcode.com/problems/n-queens-ii/

    Note: This solution is from https://time.geekbang.org/course/detail/100019701-67648.
    """

    def __init__(self):
        self.count = 0

    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 0
        self._dfs(n, 0, 0, 0, 0)
        return self.count

    def _dfs(self, n: int, row: int, col: int, left_falling: int, right_falling: int):
        if row >= n:
            self.count += 1
            return

        # Get available positions, which is represented by the '1' bit.
        bits = (~(col | left_falling | right_falling)) & ((1 << n) - 1)

        while bits:
            p = bits & -bits
            self._dfs(n, row + 1, col | p, (left_falling | p) << 1, (right_falling | p) >> 1)
            bits &= bits - 1
            bits &= bits - 1
