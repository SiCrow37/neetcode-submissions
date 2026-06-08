class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        i = 0
        ans = []

        for n in nums2:
            d[n] = i
            i += 1
        
        for n in nums1:
            i = d[n]
            while i < len(nums2):
                if n < nums2[i]:
                    ans.append(nums2[i])
                    break
                i += 1
            if i == len(nums2):
                ans.append(-1)
        
        return ans

        