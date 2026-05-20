class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = {}
        for n in nums:
            if n not in s:
                s[n] = 1
            else: s[n] += 1

        l = 0
        r = 0
        for ss in s:
            if s[ss] > l:
                l = s[ss]
                r = ss
        return r
            
