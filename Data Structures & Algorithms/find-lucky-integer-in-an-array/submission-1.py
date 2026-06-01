class Solution:
    def findLucky(self, arr: List[int]) -> int:
        s = {}
        l = -1

        for a in arr:
            if a not in s:
                s[a] = 1
            else: 
                s[a] += 1

        for ch in s:
            if ch == s[ch] and ch > l:
                l = ch

        return l
