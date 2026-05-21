class Solution:
    def scoreOfString(self, s: str) -> int:
        r = 0
        for i in range(1, len(s)):
            c = abs(ord(s[i]) - ord(s[i-1]))
            r += c
        return r