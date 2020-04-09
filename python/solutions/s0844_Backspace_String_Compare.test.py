import unittest

from s0844_Backspace_String_Compare import Solution

s = Solution()


class MyTestCase(unittest.TestCase):
    def test_n(self):
        self.assertTrue(s.backspaceCompare("ab#c", "ad#c"))
        self.assertTrue(s.backspaceCompare("ab##", "c#d#"))
        self.assertTrue(s.backspaceCompare("a##c", "#a#c"))
        self.assertFalse(s.backspaceCompare("a#c", "b"))

    def test_e1(self):
        self.assertTrue(s.backspaceCompare("y#fo##f", "y#f#o##f"))


if __name__ == '__main__':
    unittest.main()
