import unittest

from s0929_Unique_Email_Addresses import Solution

s = Solution()


class MyTestCase(unittest.TestCase):

    def test_n(self):
        self.assertEqual(2, s.numUniqueEmails(
            ["test.email+alex@leetcode.com",
             "test.e.mail+bob.cathy@leetcode.com",
             "testemail+david@lee.tcode.com"]))

    def test_e1(self):
        self.assertEqual(3, s.numUniqueEmails(
            ["testemail@leetcode.com",
             "testemail1@leetcode.com",
             "testemail+david@lee.tcode.com"]
        ))


if __name__ == '__main__':
    unittest.main()
