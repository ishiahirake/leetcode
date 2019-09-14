import unittest

from s0232_implement_queue_using_stacks import MyQueue


class MyTestCase(unittest.TestCase):

    def test_my_queue(self):
        queue = MyQueue()

        queue.push(1)
        queue.push(2)

        self.assertEqual(1, queue.peek())
        self.assertEqual(1, queue.pop())
        self.assertFalse(queue.empty())
        self.assertEqual(2, queue.pop())
        self.assertTrue(queue.empty())


if __name__ == '__main__':
    unittest.main()
