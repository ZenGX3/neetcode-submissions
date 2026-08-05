class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        self.st.append(val)

    def pop(self) -> None:
        self.st.pop(-1)

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return min(self.st)
        
