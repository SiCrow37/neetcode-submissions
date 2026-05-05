class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        left = 0
        right = len(heights) - 1
        curr = 0

        while left <= right:
            if heights[left] > heights[right]:
                curr = heights[right] * (right - left)
                if curr > m:
                    m = curr
                right -= 1
            elif heights[left] < heights[right]:
                curr = heights[left] * (right - left)
                if curr > m:
                    m = curr
                left += 1
            elif heights[left] == heights[right]:
                curr = heights[left] * (right - left)
                if curr > m:
                    m = curr
                left += 1
            
            
        return m





