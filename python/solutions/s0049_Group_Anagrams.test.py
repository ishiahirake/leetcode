import unittest

from s0049_Group_Anagrams import Solution

s = Solution()


def anagrams_str(anagrams) -> str:
    return '|'.join(sorted(['-'.join(sorted(anagram)) for anagram in anagrams]))


class MyTestCase(unittest.TestCase):
    def test_n(self):
        self.assertAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"], [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"],
        ])

    def assertAnagrams(self, strs, excepted):
        self.assertEqual(anagrams_str(excepted), anagrams_str(s.groupAnagrams(strs)))


if __name__ == '__main__':
    unittest.main()
