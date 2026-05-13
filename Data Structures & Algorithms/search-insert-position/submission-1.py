class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        u = len(nums) - 1
        l = 0
        t = target
        m = (len(nums) - 1) // 2
        
        if nums[m] != t:
            while l <= u:
                if nums[m] < t:
                    l = m + 1
                elif nums[m] > t:
                    u = m - 1
                else:
                    return m
                m = l + ((u - l) // 2) 
        else:
            return m
        
        return l
