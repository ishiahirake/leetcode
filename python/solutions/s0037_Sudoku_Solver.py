from typing import List
from collections import namedtuple
from copy import deepcopy

Board = List[List[str]]
Position = namedtuple('Position', ['row', 'col', 'digits'])


class Solution:
    """
    37. Sudoku Solver.

    :see https://leetcode.com/problems/sudoku-solver/
    """

    def solveSudoku(self, board: Board) -> None:
        is_solved = False

        def f(positions: List[Position]):
            nonlocal is_solved
            if len(positions) == 0:
                is_solved = True
                return
            positions.sort(key=lambda i: len(i.digits))
            position = positions.pop(0)
            for digit in position.digits:
                next_positions = deepcopy(positions)
                self._place_at(board, next_positions,
                               position.row, position.col, digit)
                f(next_positions)
                if is_solved:
                    return

        f(self._resolve_to_fill_positions(board))

    def _resolve_to_fill_positions(self, board: Board) -> List[Position]:
        res = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    position = self._to_fill_at(board, row, col)
                    res.append(position)
        return res

    def _to_fill_at(self, board: Board, row: int, col: int) -> List[Position]:
        digits = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        for i in range(9):
            # Row
            digits.discard(board[row][i])
            # Col
            digits.discard(board[i][col])
        r, c = (row // 3) * 3, (col // 3) * 3
        for ri in range(r, r + 3):
            for ci in range(c, c + 3):
                digits.discard(board[ri][ci])

        return Position(row=row, col=col, digits=digits)

    def _place_at(self, board: Board, positions: List[Position], row: int, col: int, val: str) -> None:
        board[row][col] = val
        for position in positions:
            if position.row == row or position.col == col \
                    or (position.row // 3 == row // 3 and position.col // 3 == col // 3):
                position.digits.discard(val)
