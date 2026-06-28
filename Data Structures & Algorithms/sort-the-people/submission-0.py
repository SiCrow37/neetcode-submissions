class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = [p[1] for p in sorted(zip(heights, names), reverse=True)]
        return l