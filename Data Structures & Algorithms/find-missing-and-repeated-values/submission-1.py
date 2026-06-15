class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d = {}
        ans = []

        for x in grid:
            for y in x:
                if y not in d:
                    d[y] = 1
                else:
                    ans.append(y)
        
        for i in range(1, (len(grid)**2) + 1):
            if i not in d:
                ans.append(i)

        return ans