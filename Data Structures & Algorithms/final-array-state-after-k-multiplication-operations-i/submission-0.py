class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        while k > 0:
            m = nums.index(min(nums))
            nums[m] *= multiplier
            k -= 1

        return nums