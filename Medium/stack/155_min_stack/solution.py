class MinStack:
    def __init__(self):
        self.stack = list()
        self.min = None

    def push(self, val: int) -> None:
        value = {"val": val, "next": None}
        if self.min:
            if val < self.min["val"]:
                value["next"] = self.min
                self.min = value
        else:
            self.min = value
        self.stack.append(value)

    def pop(self) -> None:
        value = self.stack.pop()
        if value is self.min:
            self.min = value["next"]

    def top(self) -> int:
        return self.stack[-1]["val"]

    def getMin(self) -> int:
        return self.min["val"]
