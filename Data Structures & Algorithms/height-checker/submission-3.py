class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c = 0
        h = sorted(heights)
        for i in range(len(h)):
            if h[i] != heights[i]:
                c += 1

        return c