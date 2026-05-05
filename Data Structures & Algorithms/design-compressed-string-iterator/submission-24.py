class StringIterator:

    def __init__(self, compressedString: str):
        self.s = []
        self.c = []
        self.i = 0
        self.curr = ""

        for ch in compressedString:
            if ch.isdigit():
                self.curr += ch
            else:
                if len(self.s) > 0:
                    self.c.append(int(self.curr))
                self.curr = ""
                self.s.append(ch)

    def next(self) -> str:
        val = self.s[self.i]
        self.c[self.i] -= 1
        if self.c[self.i] == 0:
            self.i += 1
        return val

    def hasNext(self) -> bool:
        if self.i < len(self.s):
            return True
        else: return False
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
