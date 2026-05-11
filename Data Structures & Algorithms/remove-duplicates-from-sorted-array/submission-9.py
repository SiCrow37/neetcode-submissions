class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = len(nums) - 1

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        while i > -1:
            if i != len(nums) - 1:
                if nums[i+1] == nums[i]:
                    del nums[i+1]
                else: 
                    k += 1
            else: k += 1
            i -= 1
        

        return k
