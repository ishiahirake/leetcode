import unittest

from s0225_implement_stack_using_queues import MyStack


class MyTestCase(unittest.TestCase):

    def test_simple(self):
        stack = MyStack()

        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.top())
        self.assertEqual(2, stack.top())
        self.assertFalse(stack.empty())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())
        self.assertTrue(stack.empty())


if __name__ == '__main__':
    unittest.main()
