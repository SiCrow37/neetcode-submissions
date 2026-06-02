class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        j = len(nums)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[j] = nums[i]
            j += 1
        return ans
