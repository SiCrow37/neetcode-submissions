class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        curr = (0, 0)
        visited = {}
        visited[(0, 0)] = 1

        for p in path:
            curr = list(curr)

            if p == 'N':
                curr[1] += 1
            elif p == 'S':
                curr[1] -= 1
            elif p == 'W':
                curr[0] -= 1
            elif p == 'E':
                curr[0] += 1

            curr = tuple(curr)
            
            if curr in visited:
                return True

            visited[curr] = 1
        
        return False
