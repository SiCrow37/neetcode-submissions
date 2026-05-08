class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans =[[], []]
        for d in nums1:
            if d not in nums2 and d not in ans[0]:
                ans[0].append(d)
        for d in nums2:
            if d not in nums1 and d not in ans[1]:
                ans[1].append(d)
        return ans
