class TrieNode:
    def __init__(self):
        self._children = {}
        self.is_terminal = False

    @property
    def children(self):
        return self._children.values()

    def setdefault_child(self, char: str, default=None):
        return self._children.setdefault(char, default if default else TrieNode())

    def get_child(self, char: str):
        return self._children.get(char)


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.node
        for char in word:
            node = node.setdefault_child(char)
        node.is_terminal = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._dfs(self.node, word)

    def _dfs(self, node, word: str) -> bool:
        if not node:
            return False
        if not word:
            return node.is_terminal

        char, left = word[0], word[1:]
        if char != '.':
            return self._dfs(node.get_child(char), left)
        else:
            for child in node.children:
                if self._dfs(child, left):
                    return True
            return False
