class MinStack:

    def __init__(self):
        self.stack =  []
        self.min_stack = []
        self.min_val = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_val = min(self.min_val, val)
        self.min_stack.append(self.min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            return None