class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        c = 0
        for i in nums:
            if i == 1:
                c += 1
                if c > m:
                    m = c
            if i == 0:
                c = 0
        return m
            