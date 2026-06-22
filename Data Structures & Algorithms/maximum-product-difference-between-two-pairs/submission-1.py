class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        s = heapq.nsmallest(2, nums)
        l = heapq.nlargest(2, nums)

        ans = (l[0] * l[1]) - (s[0] * s[1])
        return ans