class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        c = -1
        seen = dict()
        for num in nums:
            if num in seen:
                seen[num] = -1
            else:
                seen[num] = 1
        for num in seen:
            if seen[num] == -1:
                continue
            if num > c:
                c = num
        return c

            
            