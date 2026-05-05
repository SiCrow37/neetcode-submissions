class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = len(s)
        # max
        m = 0
        # left
        l = 0
        # right
        r = 1
        # current
        c = 0

        seen = dict()

        if length == 0 or length == 1:
            return length

        else:
            seen[s[l]] = 1
            c += 1
            while r < length:
                if s[r] not in seen:
                    seen[s[r]] = 1
                    c += 1
                    r += 1
                    if c > m:
                        m = c
                else: 
                    if c > m:
                        m = c
                    seen = dict()
                    c = 0
                    l += 1
                    r = l + 1
                    seen[s[l]] = 1
                    c += 1
                    
        return m


                        
