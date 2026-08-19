class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = {}

        for ss in s:
            if ss not in d:
                d[ss] = 1
            else:
                d[ss] += 1
        
        c = 0
        for k in d:
            if d[k] % 2 == 1:
                c += 1

        if c > 1:
            return False
        
        return True