class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        while i > -1:
            if m == 0:
                while n > 0:
                    nums1[i] = nums2[n-1]
                    n -= 1
                    i -= 1
            elif n == 0:
                return nums1


            elif nums1[m-1] >= nums2[n-1]:
                nums1[i] = nums1[m-1]
                nums1[m-1] = 0
                m -= 1
                i -= 1
            elif nums1[m-1] < nums2[n-1]:
                nums1[i] = nums2[n-1]
                n -= 1
                i -= 1
