class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h = len(nums) -1
        l = 0
        m = 0
     
        while l <= h:
            m = l + ((h-l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                h = m - 1 
        return -1


