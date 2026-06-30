class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        a = -1

        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = -1
            elif s[i] not in d:
                d[s[i]] = i

        for k in d:
            if d[k] != -1:
                a = d[k]
                break

        return a
