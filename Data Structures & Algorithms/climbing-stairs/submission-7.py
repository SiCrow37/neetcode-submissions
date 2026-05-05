class Solution:
    def climbStairs(self, n: int) -> int:
        l1 = 1
        l2 = 0
        c = 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            while n > 0:
                c = l1 + l2
                l2 = l1
                l1 = c
                n -= 1
        return c

