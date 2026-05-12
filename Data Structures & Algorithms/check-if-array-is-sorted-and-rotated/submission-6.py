class Solution:
    def check(self, nums: List[int]) -> bool:
        s = (nums[0], 0)
        i = 0
        n = nums

        for k in n:
            if k < s[0]:
                s = (k, i)
            i += 1

        i = 0
        while i < s[1]:
            if n[i] < n[i-1]:
                return False
            i += 1
        i = s[1]+1
        while i < len(n):
            if n[i] < n[i-1]:
                return False
            i += 1
        
        return True
                

