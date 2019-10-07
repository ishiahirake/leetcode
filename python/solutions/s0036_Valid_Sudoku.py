from typing import List


class Solution:
    """
    36. Valid Sudoku.

    :see https://leetcode.com/problems/valid-sudoku/
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            # Row
            if not self._is_valid_seq(board[i]):
                return False
            # Col
            if not self._is_valid_seq([board[x][i] for x in range(9)]):
                return False
            # 3 x 3 sub board
            if not self._is_valid_seq(self._get_sub_board_seq(board, i)):
                return False

        return True

    def _is_valid_seq(self, seq: List[str]) -> bool:
        s = set()
        for c in seq:
            if c != '.':
                if c not in s:
                    s.add(c)
                else:
                    return False
        return True

    def _get_sub_board_seq(self, board: List[List[str]], n: int) -> List[str]:
        row, col = (n // 3) * 3, (n % 3) * 3
        seq = []
        for ri in range(row, row + 3):
            for ci in range(col, col + 3):
                seq.append(board[ri][ci])
        return seq
