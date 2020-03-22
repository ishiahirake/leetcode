import unittest

from s0450_Delete_Node_in_a_BST import Solution
from lib import BinaryTreeCodec


class MyTestCase(unittest.TestCase):

    def test_f1(self):
        values = [2, 0, 33, None, 1, 25, 40, None, None, 11, 31, 34, 45, 10, 18, 29, 32, None, 36, 43, 46, 4, None, 12,
                24, 26, 30, None, None, 35, 39, 42, 44, None, 48, 3, 9, None, 14, 22, None, None, 27, None, None, None,
                None, 38, None, 41, None, None, None, 47, 49, None, None, 5, None, 13, 15, 21, 23, None, 28, 37, None,
                None, None, None, None, None, None, None, 8, None, None, None, 17, 19, None, None, None, None, None,
                None, None, 7, None, 16, None, None, 20, 6]
        key = 33

        root = BinaryTreeCodec().deserialize(values)

        s = Solution()
        s.deleteNode(root, key)

        # self.assertEqual()



if __name__ == '__main__':
    unittest.main()
