TRIE_NODE_SIZE = 26


class TrieNode:

    def __init__(self):
        self.children = [None] * TRIE_NODE_SIZE
        # is_end_of_word is True if node represent the end of the word
        self.is_end_of_word = False

    def insert_child(self, c: str):
        ci = ord(c) - ord('a')
        if self.children[ci] == None:
            self.children[ci] = TrieNode()
        return self.children[ci]

    def get_child(self, c: str):
        ci = ord(c) - ord('a')
        return self.children[ci]


class Trie:
    """
    208. Implement Trie (Prefix Tree).

    :see https://leetcode.com/problems/implement-trie-prefix-tree/
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.node
        for char in word:
            node = node.insert_child(char)
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.node
        for c in word:
            node = node.get_child(c)
            if node == None:
                return False
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.node
        for c in prefix:
            node = node.get_child(c)
            if node == None:
                return False
        return True
