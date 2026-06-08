class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s = list(s)
        d = {}
        ans = ""

        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        
        for ch in order:
            if ch in d:
                while d[ch] > 0:
                    ans += ch
                    d[ch] -= 1
            
                del d[ch]
        
        for ch in d:
            while d[ch] > 0:
                ans += ch
                d[ch] -= 1
        
        return ans
        



