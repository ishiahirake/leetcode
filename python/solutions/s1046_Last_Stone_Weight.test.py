import unittest

from s1046_Last_Stone_Weight import Solution

s = Solution()


class MyTestCase(unittest.TestCase):
    def test_n(self):
        self.assertEqual(1, s.lastStoneWeight([2, 7, 4, 1, 8, 1]))


if __name__ == '__main__':
    unittest.main()
