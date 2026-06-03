class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = {}
        r = []

        for n in nums:
            if n not in s:
                s[n] = 1
            
            else:
                r.append(n)
            
        for i in range(1, len(nums) + 1):
            if i not in s:
                r.append(i)
        
        return r
            
        