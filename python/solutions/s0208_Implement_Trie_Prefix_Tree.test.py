import unittest

from s0208_Implement_Trie_Prefix_Tree import Trie


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        trie = Trie()

        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))


if __name__ == '__main__':
    unittest.main()
