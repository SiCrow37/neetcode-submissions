class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = []
        for n in nums1:
            if n in nums2 and n not in a:
                a.append(n)
        return a