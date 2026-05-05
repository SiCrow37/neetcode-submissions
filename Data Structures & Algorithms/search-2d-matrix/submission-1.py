class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        for i in matrix:
            for j in i:
                if j == target:
                    found = True
                    return found
        return found