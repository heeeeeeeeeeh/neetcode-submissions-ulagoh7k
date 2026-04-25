class MinStack:

    def __init__(self):
        self.stack = []
        self.minS = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minS:
            self.minS.append(min(self.stack[-1], self.minS[-1]))
        else:
            self.minS.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minS.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minS[-1]