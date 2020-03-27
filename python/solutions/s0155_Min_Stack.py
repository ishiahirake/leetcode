class MinStack:
    """
    155. Min Stack.

    :see https://leetcode.com/problems/min-stack/
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []

    def push(self, x: int) -> None:
        min_val = x if not self.values or x < self.getMin() else self.getMin()
        self.values.append([x, min_val])

    def pop(self) -> None:
        self.values[-1:] = []

    def top(self) -> int:
        return self.values[-1][0]

    def getMin(self) -> int:
        return self.values[-1][1]
