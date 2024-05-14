class MinStack:
    def __init__(self):
        self.mini_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mini_stack)==0 or val <= self.mini_stack[-1]:
            self.mini_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return None
        popped_element = self.stack.pop()
        if popped_element == self.mini_stack[-1]:
            self.mini_stack.pop()
        else:
            return popped_element
        
    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.mini_stack:
            return None
        return self.mini_stack[-1]
