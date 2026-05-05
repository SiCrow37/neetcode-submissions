class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current = dict()
        for i in nums:
            if i in current:
                return True
            else:
                current[i] = 1
        return False

