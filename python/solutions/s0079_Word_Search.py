from typing import List
from collections import namedtuple

Board = List[List[str]]
Position = namedtuple("Position", ['x', 'y'])


class Solution:
    """
    79. Word Search.

    :see ;https://leetcode.com/problems/word-search/
    """

    def exist(self, board: Board, word: str) -> bool:
        if not word:
            return False
        row_count, col_count = len(board), len(board[0])

        for row in range(row_count):
            for col in range(col_count):
                if board[row][col] == word[0]:
                    pos = Position(x=row, y=col)
                    used_pos = set([pos])
                    if self._backtace(board, pos, word[1:], used_pos):
                        return True
        return False

    def _backtace(self, board: Board, pos: Position, word: str, used_pos: set) -> bool:
        if not word:
            return True

        char = word[0]
        for adjacent_position in self._get_adjacent_positions(board, pos, used_pos):
            if board[adjacent_position.x][adjacent_position.y] == char \
                    and adjacent_position not in used_pos:
                used_pos.add(adjacent_position)
                if self._backtace(board, adjacent_position, word[1:], used_pos):
                    return True
                else:
                    used_pos.remove(adjacent_position)

        return False

    def _get_adjacent_positions(self, board: Board, pos: Position, used_pos: set) -> List[Position]:
        result, xlimit, ylimit = [], len(board), len(board[0])
        if pos.x - 1 >= 0:
            result.append(Position(x=pos.x-1, y=pos.y))
        if pos.y + 1 < ylimit:
            result.append(Position(x=pos.x, y=pos.y+1))
        if pos.x + 1 < xlimit:
            result.append(Position(x=pos.x+1, y=pos.y))
        if pos.y - 1 >= 0:
            result.append(Position(x=pos.x, y=pos.y-1))
        return result
