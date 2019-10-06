from typing import List
from copy import deepcopy

# chessboard type alias
Chessboard = List[List[str]]


class Solution:
    """
    51. N-Queens.

    :see https://leetcode.com/problems/n-queens/.
    """

    def totalNQueens(self, n: int) -> List[List[str]]:
        total_n_queens = 0

        def backtrack(chessboard: Chessboard, level: int = 0):
            nonlocal total_n_queens
            if level == n:
                total_n_queens += 1
                return
            for idx, val in enumerate(chessboard[level]):
                if val != 'x':
                    backtrack(
                        self._place_queen(deepcopy(chessboard), level, idx),
                        level + 1
                    )

        backtrack([['.' for x in range(n)] for y in range(n)])

        return total_n_queens

    def _place_queen(self, chessboard: Chessboard, row: int, col: int) -> Chessboard:
        n = len(chessboard)
        chessboard[row][col] = 'Q'
        # |
        for i in range(row + 1, n):
            chessboard[i][col] = 'x'
        # /
        ri, ci = row + 1, col - 1
        while ri < n and ci >= 0:
            chessboard[ri][ci] = 'x'
            ri += 1
            ci -= 1
        # \
        ri, ci = row + 1, col + 1
        while ri < n and ci < n:
            chessboard[ri][ci] = 'x'
            ri += 1
            ci += 1
        return chessboard
