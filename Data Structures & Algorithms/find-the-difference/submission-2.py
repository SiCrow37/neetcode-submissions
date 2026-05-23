class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}

        for c in s:
            if c not in d:
                d[c] = 1
            else: d[c] += 1
        
        for c in t:
            if c in d:
                d[c] -= 1
                if d[c] == 0:
                    del d[c]
            else: return c