import unittest

from s0155_Min_Stack import MinStack


class MyTestCase(unittest.TestCase):

    def test_n(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        self.assertEqual(-3, stack.getMin())
        stack.pop()

        self.assertEqual(0, stack.top())
        self.assertEqual(-2, stack.getMin())


if __name__ == '__main__':
    unittest.main()
