from collections import deque


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = deque()
        self.output = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self._ensure_output()
        return self.output.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self._ensure_output()
        return self.output[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.input) == 0 and len(self.output) == 0

    def _ensure_output(self):
        if len(self.output) > 0:
            return

        for i in range(len(self.input)):
            self.output.append(self.input.pop())
