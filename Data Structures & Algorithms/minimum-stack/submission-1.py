class MinStack:

    def __init__(self):
        self.l = []

    def push(self, val: int) -> None:
        if len(self.l) == 0: 
            self.l.append((val, val))
        else:
            v, m = self.l[-1]
            self.l.append((val, min(m, val)))

    def pop(self) -> None:
        self.l.pop()

    def top(self) -> int:
        val, m = self.l[-1]
        return val

    def getMin(self) -> int:
        val, m = self.l[-1]
        return m
        
