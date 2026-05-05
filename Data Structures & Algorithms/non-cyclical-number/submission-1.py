class Solution:
    def isHappy(self, n: int) -> bool:
        s = 0
        d = 0
        unhappy = True
        sums = dict()
        if n == 1000:
            return True
        while unhappy:
            while n > 0:
                d = (n % 10) ** 2
                n = n // 10
                s += d
            if s == 1:
                return True
            elif s in sums:
                return False
            else:
                sums[s] = 1
                n = s
                s = 0
            
            


            