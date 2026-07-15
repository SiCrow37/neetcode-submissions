class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 9 minutes and 25 seconds completion time
        j = 0
        arr = []
        mapping = dict()
        for num in nums2:
            if num not in mapping:
                mapping[num] = j
            j += 1
        for num in nums1:
            if num in mapping:
                arr.append(mapping[num])
        return arr