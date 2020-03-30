import unittest

from s0003_Longest_Substring_Without_Repeating_Characters import Solution

s = Solution()


class MyTestCase(unittest.TestCase):

    def test_n(self):
        self.assertEqual(3, s.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, s.lengthOfLongestSubstring("bbbbb"))
        self.assertEqual(3, s.lengthOfLongestSubstring("pwwkew"))

    def test_e1(self):
        self.assertEqual(2, s.lengthOfLongestSubstring("aab"))


if __name__ == '__main__':
    unittest.main()
