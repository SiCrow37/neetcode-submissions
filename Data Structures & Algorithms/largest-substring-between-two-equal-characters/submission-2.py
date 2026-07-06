class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        m = -1

        for ch in s:
            if ch not in d:
                for k in d:
                    d[k] += 1
                d[ch] = 0
            else:
                if d[ch] > m:
                    m = d[ch]
                for k in d:
                    d[k] += 1
                
        return m
