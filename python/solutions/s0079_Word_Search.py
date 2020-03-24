from typing import List


class Solution:
    """
    79. Word Search.

    :see ;https://leetcode.com/problems/word-search/
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        row, col = len(board), len(board[0])
        for ri in range(row):
            for ci in range(col):
                if self._dfs(board, ri, ci, '', word):
                    return True

        return False

    def _dfs(self, board: List[List[str]], ri: int, ci: int, word: str, target: str) -> bool:
        row, col = len(board), len(board[0])
        if not self._is_between(ri, 0, row - 1) or not self._is_between(ci, 0, col - 1):
            return False

        char = board[ri][ci]
        if char == '#':
            return False

        word = word + char
        if not target.startswith(word):
            return False

        if word == target:
            return True

        board[ri][ci] = '#'

        is_found = False
        if self._dfs(board, ri - 1, ci, word, target) \
                or self._dfs(board, ri + 1, ci, word, target) \
                or self._dfs(board, ri, ci - 1, word, target) \
                or self._dfs(board, ri, ci + 1, word, target):
            is_found = True

        board[ri][ci] = char

        return is_found

    @staticmethod
    def _is_between(val, min_val, max_val) -> bool:
        return min_val <= val <= max_val
