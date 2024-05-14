class MinStack:
    def __init__(self):
        self.mini = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.mini = val
        else:
            if val<self.mini:
                self.stack.append(2*val-self.mini)
                self.mini = val
            else:
                self.stack.append(val)
        
    def pop(self) -> None:
        if not self.stack:
            return 
        v = self.stack.pop()
        if v< self.mini:
            self.mini = 2*self.mini - v
        
    def top(self) -> int:
        v = self.stack[-1]
        if v<self.mini:
            return self.mini
        return v

    def getMin(self) -> int:
        return self.mini
