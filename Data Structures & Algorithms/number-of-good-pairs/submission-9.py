class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        c = 0
        i = 0
        j = 1

        while i < len(nums) - 1:
            while j < len(nums):
                if nums[i] == nums[j]:
                    c += 1
                j += 1
            i += 1
            j = i+1
        
        return c