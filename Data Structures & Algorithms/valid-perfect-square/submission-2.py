class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        l = 0

        while l <= r:
            m = l + ((r - l) // 2)
            if m * m == num:
                return True
            elif m * m < num:
                l = m + 1
            elif m * m > num:
                r = m - 1
        
        return False
