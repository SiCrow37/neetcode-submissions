class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        groups = [0, 0, 0]

        for num in nums:
            groups[num] += 1

        i = 0
        l = 0
        for j in groups:
            while j > 0:
                nums[i] = l
                i+=1
                j-=1
            l += 1