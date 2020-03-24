from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_terminal = False

    def setdefault_child(self, char: str, default=None):
        return self.children.setdefault(char, default if default else TrieNode())

    def get_child(self, char: str):
        return self.children.get(char)


class Trie:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.node
        for char in word:
            node = node.setdefault_child(char)
        node.is_terminal = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._find(word)
        return node is not None and node.is_terminal

    def starts_with(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._find(prefix) is not None

    def _find(self, prefix: str):
        """Find the node that starts with the given prefix, or None when not found.
        :param str prefix:
        :return:
        """
        node = self.node
        for char in prefix:
            node = node.get_child(char)
            if node is None:
                return None
        return node


def is_between(val, min_val, max_val) -> bool:
    return min_val <= val <= max_val


class Solution:
    """
    212. Word Search II.

    :see https://leetcode.com/problems/word-search-ii/
    """

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []

        trie = Trie()
        for word in words:
            trie.insert(word)

        exists = set()

        row, col = len(board), len(board[0])
        for ri in range(row):
            for ci in range(col):
                self._dfs(board, ri, ci, '', trie, exists)

        return list(exists)

    def _dfs(self, board: List[List[str]], ri: int, ci: int, word: str, trie: Trie, exists):
        row, col = len(board), len(board[0])
        if not is_between(ri, 0, row - 1) or not is_between(ci, 0, col - 1):
            return

        char = board[ri][ci]
        if char == '#':
            return

        word = word + char

        if not trie.starts_with(word):
            return

        if trie.search(word):
            exists.add(word)

        board[ri][ci] = '#'

        self._dfs(board, ri - 1, ci, word, trie, exists)
        self._dfs(board, ri + 1, ci, word, trie, exists)
        self._dfs(board, ri, ci - 1, word, trie, exists)
        self._dfs(board, ri, ci + 1, word, trie, exists)

        board[ri][ci] = char
