class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.stack = deque()

        if len(self.nums) != 0:
            for n in self.nums:
                h = []
                if len(self.stack) == 0:
                    self.stack.append(n)
                elif len(self.stack) < k:
                    if n > self.stack[-1]:
                        self.stack.append(n)
                    elif n < self.stack[0]:
                        self.stack.appendleft(n)
                    else:
                        while n > self.stack[0]:
                            h.append(self.stack.popleft())
                        self.stack.appendleft(n)
                        while len(h) > 0:
                            self.stack.appendleft(h.pop())
                elif len(self.stack) == k:
                    if n >= self.stack[-1]:
                        self.stack.append(n)
                        self.stack.popleft()
                    elif n > self.stack[0]:
                        self.stack.popleft()
                        if n <= self.stack[0]:
                            self.stack.appendleft(n)
                        else:
                            while n > self.stack[0]:
                                h.append(self.stack.popleft())
                            self.stack.appendleft(n)
                            while len(h) > 0:
                                self.stack.appendleft(h.pop())


    def add(self, val: int) -> int:
        h = []
        print(self.stack)
        if len(self.stack) == 0:
            self.stack.append(val)
        elif len(self.stack) < self.k:
            if val > self.stack[-1]:
                self.stack.append(val)
            elif val < self.stack[0]:
                self.stack.appendleft(val)
            else:
                while val > self.stack[0]:
                    h.append(self.stack.popleft())
                self.stack.appendleft(val)
                while len(h) > 0:
                    self.stack.appendleft(h.pop())
        elif len(self.stack) == self.k:
            if val >= self.stack[-1]:
                self.stack.append(val)
                self.stack.popleft()
            elif val > self.stack[0]:
                self.stack.popleft()
                if val <= self.stack[0]:
                    self.stack.appendleft(val)
                else:
                    while val > self.stack[0]:
                        h.append(self.stack.popleft())
                    self.stack.appendleft(val)
                    while len(h) > 0:
                        self.stack.appendleft(h.pop())
        return self.stack[0]



        
