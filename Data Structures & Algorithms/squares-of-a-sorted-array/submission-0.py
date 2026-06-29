class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = sorted(n * n for n in nums)
        return l