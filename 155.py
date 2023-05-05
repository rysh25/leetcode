from typing import List


class MinStack:
    def __init__(self):
        self.s: List[int] = []
        self.min_s: List[int] = []

    def push(self, val: int) -> None:
        self.s.append(val)
        val = min(val, self.min_s[-1] if self.min_s else val)
        self.min_s.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.min_s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(0)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
