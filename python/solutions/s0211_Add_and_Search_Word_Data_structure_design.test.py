import unittest

from s0211_Add_and_Search_Word_Data_structure_design import WordDictionary


class MyTestCase(unittest.TestCase):

    def test_n(self):
        wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        wd.addWord("mad")

        self.assertFalse(wd.search("pad"))
        self.assertTrue(wd.search("bad"))
        self.assertTrue(wd.search(".ad"))
        self.assertTrue(wd.search("b.."))


if __name__ == '__main__':
    unittest.main()
