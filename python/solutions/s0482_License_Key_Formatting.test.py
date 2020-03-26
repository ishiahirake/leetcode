import unittest

from s0482_License_Key_Formatting import Solution

s = Solution()


class MyTestCase(unittest.TestCase):

    def test_n(self):
        self.assertEqual('5F3Z-2E9W', s.licenseKeyFormatting('5F3Z-2e-9-w', 4))
        self.assertEqual('2-5G-3J', s.licenseKeyFormatting('2-5g-3-J', 2))


if __name__ == '__main__':
    unittest.main()
