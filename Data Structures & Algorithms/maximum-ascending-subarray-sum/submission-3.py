class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        m = 0
        c = nums[0]

        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                c += nums[i]
                if c > m:
                    m = c
            
            elif nums[i] <= nums[i-1]:
                
                if c > m:
                    m = c

                c = nums[i]

        return m
                






