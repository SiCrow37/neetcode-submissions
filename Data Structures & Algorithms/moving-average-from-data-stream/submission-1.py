class MovingAverage:

    def __init__(self, size: int):
        self.s = size
        self.w = deque()

    def next(self, val: int) -> float:
        summ = 0
        if len(self.w) < self.s:
            self.w.append(val)
        else: 
            self.w.append(val)
            self.w.popleft()

        for ww in self.w:
            summ += ww
        summ /= len(self.w)
        return summ

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
