class Solution:
    def climbStairs(self, n: int) -> int:
        l1 = 1
        l2 = 0
        c = 0

    
        while n > 0:
            c = l1 + l2
            l2 = l1
            l1 = c
            n -= 1
        return c

