class RandomizedSet:

    def __init__(self):
        self.d = {}

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.d[val] = 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.d:
            del self.d[val]
            return True
        return False

    def getRandom(self) -> int:
        l = [k for k in self.d]
        r = random.randint(0, len(l)-1)
        return l[r]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()