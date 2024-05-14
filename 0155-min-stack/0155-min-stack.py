class MinStack:
    def __init__(self):
        self.mini_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mini_stack or val <= self.mini_stack[-1]:
            self.mini_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return None
        if self.stack.pop() == self.mini_stack[-1]:
            self.mini_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.mini_stack:
            return None
        return self.mini_stack[-1]
