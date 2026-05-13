class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = {}
        t = True

        for n in nums:
            if n not in s:
                s[n] = 1
                t = False
            else:
                s[n] += 1
                if s[n] % 2 == 0:
                    t = True
                else: 
                    t = False
        for v in s.values():
            if v % 2 != 0:
                t = False
        return t
            