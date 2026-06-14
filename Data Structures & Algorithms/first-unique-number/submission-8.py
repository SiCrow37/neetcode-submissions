class FirstUnique:

    def __init__(self, nums: List[int]):
        self.que = nums
        self.d = {}

        for n in self.que:
            if n not in self.d:
                self.d[n] = 1
            else:
                self.d[n] += 1
        return None

    def showFirstUnique(self) -> int:
        for n in self.que:
            if self.d[n] == 1:
                return n
        return -1
            

    def add(self, value: int) -> None:
        self.que.append(value)
        if value not in self.d:
            self.d[value] = 1
        else: 
            self.d[value] += 1
        return None
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
