class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        low = -1
        d = dict()
        for n in nums:
            if n > 0 and n not in d:
                d[n] = 1
                if low == -1:
                    low = 1
                while low in d:
                    low += 1

            if n < 0:
                if low == -1:
                    low = 1
                continue

        return low
        
            