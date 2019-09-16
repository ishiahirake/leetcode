import unittest

from s0242_valid_anagram import Solution

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(solution.isAnagram('anagram', 'nagaram'))
        self.assertFalse(solution.isAnagram('rat', 'car'))


if __name__ == '__main__':
    unittest.main()
