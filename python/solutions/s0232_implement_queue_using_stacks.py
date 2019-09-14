from collections import deque


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()
        self._assist_stack = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self._pop_to_assist(self.size - 1)
        ele = self.stack.pop()
        self._restore_to_stack()
        return ele

    def peek(self) -> int:
        """
        Get the front element.
        """
        self._pop_to_assist(self.size - 1)
        ele = self.stack[-1]
        self._restore_to_stack()
        return ele

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.size == 0

    @property
    def size(self) -> int:
        return len(self.stack)

    def _pop_to_assist(self, n: int):
        for i in range(n):
            self._assist_stack.append(self.stack.pop())

    def _restore_to_stack(self, n: int = None):
        n = n or len(self._assist_stack)
        for i in range(n):
            self.stack.append(self._assist_stack.pop())
