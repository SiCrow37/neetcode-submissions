class Solution:
    def maxDifference(self, s: str) -> int:
        d = {}

        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
            
        odd = 0
        even = float('inf')
        for k in d:
            if d[k]%2 == 1:
                if d[k] > odd:
                    odd = d[k]
            elif d[k]%2 == 0:
                if d[k] < even:
                    even = d[k]

        return odd - even